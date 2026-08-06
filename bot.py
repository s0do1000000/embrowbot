# -*- coding: utf-8 -*-
"""
Telegram-бот для курса «EmSystem by Yevgeniya Em».
"""

import asyncio
import logging
import os

from aiohttp import web
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

import config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# ============================================================
# ВСПОМОГАТЕЛЬНОЕ: получение текстов на выбранном языке
# ============================================================

def get_lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    return context.user_data.get("lang", config.DEFAULT_LANG)


def t(context: ContextTypes.DEFAULT_TYPE) -> dict:
    lang = get_lang(context)
    return config.TEXTS.get(lang, config.TEXTS[config.DEFAULT_LANG])


# ============================================================
# КЛАВИАТУРЫ
# ============================================================

def language_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(label, callback_data=f"lang:{code}")]
        for code, label in config.LANGUAGES.items()
    ]
    return InlineKeyboardMarkup(buttons)


def main_menu_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(texts["btn_about"], callback_data="menu:about")],
        [InlineKeyboardButton(texts["btn_free_lesson"], callback_data="menu:free_lesson")],
        [InlineKeyboardButton(texts["btn_works"], callback_data="menu:works")],
        [InlineKeyboardButton(texts["btn_faq"], callback_data="menu:faq")],
        [InlineKeyboardButton(texts["btn_buy"], callback_data="menu:buy")],
    ]
    return InlineKeyboardMarkup(buttons)


def about_footer_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(texts["btn_watch_free_lesson"], callback_data="menu:free_lesson")],
        [InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root")],
    ]
    return InlineKeyboardMarkup(buttons)


def free_lesson_footer_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(texts["btn_to_buy"], callback_data="menu:buy")],
        [InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root")],
    ]
    return InlineKeyboardMarkup(buttons)


def buy_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(texts["btn_buy"], url=config.BUY_URL)],
        [InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root")],
    ]
    return InlineKeyboardMarkup(buttons)


def works_footer_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(texts["btn_buy"], callback_data="menu:buy")],
        [InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root")],
    ]
    return InlineKeyboardMarkup(buttons)


def faq_list_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(short, callback_data=f"faq:{i}")]
        for i, (short, _q, _a) in enumerate(texts["faq_items"])
    ]
    buttons.append([InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root")])
    return InlineKeyboardMarkup(buttons)


def faq_answer_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(texts["btn_back_to_faq"], callback_data="menu:faq")],
        [InlineKeyboardButton(texts["btn_buy"], callback_data="menu:buy")],
        [InlineKeyboardButton(texts["btn_home"], callback_data="menu:root")],
    ]
    return InlineKeyboardMarkup(buttons)


# ============================================================
# ВСПОМОГАТЕЛЬНОЕ: отправка одиночного видео
# ============================================================

async def send_course_video(chat_id, context: ContextTypes.DEFAULT_TYPE, which: str):
    texts = t(context)

    if which == "about":
        file_id = getattr(config, "VIDEO_ABOUT_FILE_ID", None)
        path = getattr(config, "VIDEO_ABOUT_PATH", None)
    elif which == "lesson":
        file_id = getattr(config, "VIDEO_LESSON_FILE_ID", None)
        path = getattr(config, "VIDEO_LESSON_PATH", None)
    else:
        file_id = None
        path = None

    try:
        if file_id:
            await context.bot.send_video(chat_id=chat_id, video=file_id, supports_streaming=True)
            return
        if path and os.path.exists(path):
            with open(path, "rb") as f:
                await context.bot.send_video(chat_id=chat_id, video=f, supports_streaming=True)
            return
        logger.warning("Видео не найдено ни по file_id, ни по пути %s", path)
        await context.bot.send_message(chat_id=chat_id, text=texts["video_unavailable"])
    except Exception:
        logger.exception("Ошибка при отправке видео (%s)", which)
        await context.bot.send_message(chat_id=chat_id, text=texts["video_send_failed"])


# ============================================================
# ЭКРАНЫ
# ============================================================

async def show_welcome(chat_id, context: ContextTypes.DEFAULT_TYPE):
    texts = config.TEXTS[config.DEFAULT_LANG]
    await context.bot.send_message(
        chat_id=chat_id,
        text=texts["welcome_text"],
        reply_markup=language_keyboard(),
    )


async def show_main_menu(chat_id, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"{texts['brand_header']}\n\n{texts['main_menu_header']}",
        reply_markup=main_menu_keyboard(context),
    )


async def show_about(chat_id, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    await context.bot.send_message(chat_id=chat_id, text=texts["brand_header"])
    await send_course_video(chat_id, context, "about")
    await context.bot.send_message(
        chat_id=chat_id,
        text=texts["about_caption"],
        reply_markup=about_footer_keyboard(context),
    )


async def show_free_lesson(chat_id, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    await context.bot.send_message(chat_id=chat_id, text=texts["free_lesson_intro"])
    await send_course_video(chat_id, context, "lesson")
    await context.bot.send_message(
        chat_id=chat_id,
        text=texts["free_lesson_after"],
        reply_markup=free_lesson_footer_keyboard(context),
    )


async def show_works(chat_id, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    media_items = getattr(config, "WORKS_MEDIA", [])

    if media_items:
        input_media = []
        for item in media_items:
            m_type = item.get("type")
            f_id = item.get("file_id")
            if m_type == "video":
                input_media.append(InputMediaVideo(media=f_id))
            elif m_type == "photo":
                input_media.append(InputMediaPhoto(media=f_id))

        chunk_size = 10
        for i in range(0, len(input_media), chunk_size):
            chunk = input_media[i:i + chunk_size]
            try:
                await context.bot.send_media_group(chat_id=chat_id, media=chunk)
            except Exception:
                logger.exception("Ошибка при отправке альбома работ учеников")

    await context.bot.send_message(
        chat_id=chat_id,
        text=texts["student_works_text"],
        reply_markup=works_footer_keyboard(context),
    )


async def show_faq_list(chat_id, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    await context.bot.send_message(
        chat_id=chat_id,
        text=texts["faq_intro_text"],
        reply_markup=faq_list_keyboard(context),
    )


async def show_faq_answer(chat_id, context: ContextTypes.DEFAULT_TYPE, index: int):
    texts = t(context)
    short, question, answer = texts["faq_items"][index]
    text = f"❓ {question}\n\n{answer}"
    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=faq_answer_keyboard(context),
    )


async def show_buy(chat_id, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    await context.bot.send_message(
        chat_id=chat_id,
        text=texts["buy_text"],
        reply_markup=buy_keyboard(context),
    )


# ============================================================
# ХЕНДЛЕРЫ
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_welcome(update.effective_chat.id, context)


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    chat_id = query.message.chat_id

    if data.startswith("lang:"):
        lang_code = data.split(":", 1)[1]
        if lang_code not in config.LANGUAGES:
            lang_code = config.DEFAULT_LANG
        context.user_data["lang"] = lang_code
        await show_main_menu(chat_id, context)
        return

    if data == "menu:root":
        await show_main_menu(chat_id, context)
        return

    if data == "menu:about":
        await show_about(chat_id, context)
        return

    if data == "menu:free_lesson":
        await show_free_lesson(chat_id, context)
        return

    if data == "menu:works":
        await show_works(chat_id, context)
        return

    if data == "menu:faq":
        await show_faq_list(chat_id, context)
        return

    if data == "menu:buy":
        await show_buy(chat_id, context)
        return

    if data.startswith("faq:"):
        index = int(data.split(":", 1)[1])
        await show_faq_answer(chat_id, context, index)
        return

    logger.warning("Неизвестный callback_data: %s", data)


async def on_unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    await update.message.reply_text(texts["unknown_command"])


def build_application() -> Application:
    if not config.BOT_TOKEN or "ВСТАВЬТЕ_СЮДА" in config.BOT_TOKEN:
        raise RuntimeError("Не задан токен бота.")

    application = Application.builder().token(config.BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(on_callback))

    return application


# ============================================================
# DUMMY HTTP-СЕРВЕР И ЗАПУСК
# ============================================================

async def handle_ping(request):
    return web.Response(text="Bot is running!")


async def start_web_server():
    port = int(os.environ.get("PORT", 10000))
    app_web = web.Application()
    app_web.router.add_get("/", handle_ping)
    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info("HTTP dummy-сервер запущен на порту %s", port)


async def main_async():
    await start_web_server()
    application = build_application()
    logger.info("Бот запущен. Ожидание сообщений...")
    
    await application.initialize()
    await application.start()
    await application.updater.start_polling(allowed_updates=Update.ALL_TYPES)

    stop_event = asyncio.Event()
    await stop_event.wait()


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()