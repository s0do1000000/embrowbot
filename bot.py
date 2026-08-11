# -*- coding: utf-8 -*-
"""
Telegram-бот для курса EmSystem by Yevgeniya Em
"""

import logging
import os

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)
from telegram.request import HTTPXRequest

import config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# ============================================================
# ВСПОМОГАТЕЛЬНОЕ получение текстов на выбранном языке
# ============================================================

def get_lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    """Возвращает код языка пользователя, либо язык по умолчанию."""
    return context.user_data.get("lang", config.DEFAULT_LANG)


def t(context: ContextTypes.DEFAULT_TYPE) -> dict:
    """Возвращает словарь текстов config.TEXTS для текущего языка пользователя."""
    lang = get_lang(context)
    return config.TEXTS.get(lang, config.TEXTS[config.DEFAULT_LANG])


# ============================================================
# КЛАВИАТУРЫ
# ============================================================

def language_keyboard(context: ContextTypes.DEFAULT_TYPE = None, show_back: bool = False) -> InlineKeyboardMarkup:
    grid = [["en", "ru"], ["fr", "it"]]
    buttons = []
    for row_codes in grid:
        row = [
            InlineKeyboardButton(config.LANGUAGES[code], callback_data=f"lang:{code}")
            for code in row_codes
            if code in config.LANGUAGES
        ]
        if row:
            buttons.append(row)
    if show_back and context is not None:
        texts = t(context)
        buttons.append([InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root")])
    return InlineKeyboardMarkup(buttons)


def home_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(texts["btn_watch_free_lesson"], callback_data="menu:free_lesson")],
    ]
    return InlineKeyboardMarkup(buttons)


def free_lesson_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [
            InlineKeyboardButton(texts["btn_works"], callback_data="menu:works"),
            InlineKeyboardButton(texts["btn_faq"], callback_data="menu:faq"),
        ],
        [
            InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root"),
            InlineKeyboardButton(texts["btn_language"], callback_data="menu:language"),
        ],
        [InlineKeyboardButton(texts["btn_buy"], callback_data="menu:buy")],
    ]
    return InlineKeyboardMarkup(buttons)


def buy_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(texts["btn_buy"], url=config.BUY_URL)],
        [InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root")],
    ]
    return InlineKeyboardMarkup(buttons)


def works_menu_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = [
        [InlineKeyboardButton(texts["btn_works_before_after"], callback_data="works:before_after:0")],
        [InlineKeyboardButton(texts["btn_works_reviews"], callback_data="works:reviews:0")],
        [InlineKeyboardButton(texts["btn_works_certificates"], callback_data="works:certificates:0")],
        [InlineKeyboardButton(texts["btn_works_videos"], callback_data="works:videos:0")],
        [InlineKeyboardButton(texts["btn_buy"], callback_data="menu:buy")],
        [InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root")],
    ]
    return InlineKeyboardMarkup(buttons)


def works_category_footer_keyboard(
    context: ContextTypes.DEFAULT_TYPE, category: str, next_offset: int = None
) -> InlineKeyboardMarkup:
    texts = t(context)
    buttons = []
    if next_offset is not None:
        buttons.append(
            [InlineKeyboardButton(texts["btn_works_more"], callback_data=f"works:{category}:{next_offset}")]
        )
    buttons.append([InlineKeyboardButton(texts["btn_works"], callback_data="menu:works")])
    buttons.append([InlineKeyboardButton(texts["btn_buy"], callback_data="menu:buy")])
    buttons.append([InlineKeyboardButton(texts["btn_main_menu"], callback_data="menu:root")])
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
# ВСПОМОГАТЕЛЬНОЕ отправка видео
# ============================================================

async def send_course_video(
    chat_id,
    context: ContextTypes.DEFAULT_TYPE,
    which: str,
    reply_markup: InlineKeyboardMarkup = None,
):
    """
    which: "about" или "lesson"
    Для каждого языка своё видео (config.VIDEO_*_FILE_ID_BY_LANG /
    config.VIDEO_*_PATH_BY_LANG). Если для текущего языка file_id/путь
    не заполнены - используется видео языка по умолчанию (config.DEFAULT_LANG).
    """
    texts = t(context)
    lang = get_lang(context)

    if which == "about":
        file_id_map = config.VIDEO_ABOUT_FILE_ID_BY_LANG
        path_map = config.VIDEO_ABOUT_PATH_BY_LANG
    else:
        file_id_map = config.VIDEO_LESSON_FILE_ID_BY_LANG
        path_map = config.VIDEO_LESSON_PATH_BY_LANG

    # Видео для текущего языка, а если для него ничего не заполнено —
    # берём видео языка по умолчанию (чтобы не показывать пустой экран).
    file_id = file_id_map.get(lang) or file_id_map.get(config.DEFAULT_LANG)
    path = path_map.get(lang) or path_map.get(config.DEFAULT_LANG)

    try:
        if file_id:
            await context.bot.send_video(
                chat_id=chat_id, video=file_id, supports_streaming=True, reply_markup=reply_markup
            )
            return
        if path and os.path.exists(path):
            with open(path, "rb") as f:
                await context.bot.send_video(
                    chat_id=chat_id, video=f, supports_streaming=True, reply_markup=reply_markup
                )
            return
        logger.warning("Видео (%s, lang=%s) не найдено ни по file_id, ни по пути %s", which, lang, path)
        await context.bot.send_message(chat_id=chat_id, text=texts["video_unavailable"], reply_markup=reply_markup)
    except Exception:
        logger.exception("Ошибка при отправке видео (%s, lang=%s)", which, lang)
        await context.bot.send_message(chat_id=chat_id, text=texts["video_send_failed"], reply_markup=reply_markup)


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
    await send_course_video(chat_id, context, "about")
    await context.bot.send_message(
        chat_id=chat_id,
        text=texts["about_caption"],
        reply_markup=home_keyboard(context),
    )


async def show_free_lesson(chat_id, context: ContextTypes.DEFAULT_TYPE):
    await send_course_video(chat_id, context, "lesson", reply_markup=free_lesson_keyboard(context))


async def show_works(chat_id, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    await context.bot.send_message(
        chat_id=chat_id,
        text=texts["student_works_text"],
        reply_markup=works_menu_keyboard(context),
    )


async def show_works_category(chat_id, context: ContextTypes.DEFAULT_TYPE, category: str, offset: int):
    texts = t(context)
    cat_data = config.WORKS_CATEGORIES.get(category)
    if not cat_data:
        logger.warning("Неизвестная категория работ %s", category)
        return

    items = cat_data["items"]
    media_type = cat_data["type"]
    page_size = config.WORKS_PHOTOS_PAGE_SIZE
    chunk = items[offset:offset + page_size]
    remaining_after = items[offset + page_size:]
    next_offset = offset + page_size if remaining_after else None

    intro_key = f"works_{category}_intro"
    if offset == 0 and intro_key in texts:
        await context.bot.send_message(chat_id=chat_id, text=texts[intro_key])

    if not chunk:
        await context.bot.send_message(
            chat_id=chat_id,
            text=texts["works_photos_done"],
            reply_markup=works_category_footer_keyboard(context, category, next_offset=None),
        )
        return

    try:
        if len(chunk) == 1:
            f_id = chunk[0]
            if media_type == "video":
                await context.bot.send_video(chat_id=chat_id, video=f_id, supports_streaming=True)
            else:
                await context.bot.send_photo(chat_id=chat_id, photo=f_id)
        else:
            media_group = [
                InputMediaVideo(media=f_id) if media_type == "video" else InputMediaPhoto(media=f_id)
                for f_id in chunk
            ]
            await context.bot.send_media_group(chat_id=chat_id, media=media_group)
    except Exception:
        logger.exception("Ошибка при отправке медиа категории %s", category)
        await context.bot.send_message(chat_id=chat_id, text=texts["video_send_failed"])

    if next_offset is not None:
        await context.bot.send_message(
            chat_id=chat_id,
            text=texts["works_continue_prompt"],
            reply_markup=works_category_footer_keyboard(context, category, next_offset=next_offset),
        )
    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text=texts["works_photos_done"],
            reply_markup=works_category_footer_keyboard(context, category, next_offset=None),
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
    _short, question, answer = texts["faq_items"][index]
    text = f"❓ {question}\n\n{answer}"
    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=faq_answer_keyboard(context),
    )


async def show_language_select(chat_id, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    await context.bot.send_message(
        chat_id=chat_id,
        text=texts["choose_language_text"],
        reply_markup=language_keyboard(context, show_back=True),
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

    if data in ("menu:root", "menu:about"):
        await show_main_menu(chat_id, context)
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

    if data == "menu:language":
        await show_language_select(chat_id, context)
        return

    if data.startswith("works:"):
        parts = data.split(":")
        if len(parts) == 3:
            _, category, offset_str = parts
            try:
                offset = int(offset_str)
            except ValueError:
                offset = 0
            await show_works_category(chat_id, context, category, offset)
        return

    if data.startswith("faq:"):
        index = int(data.split(":", 1)[1])
        await show_faq_answer(chat_id, context, index)
        return

    logger.warning("Неизвестный callback_data %s", data)


async def on_unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texts = t(context)
    await update.message.reply_text(texts["unknown_command"])


def build_application():
    # Проверка вызова токена без падения при совпадении со значениями по умолчанию
    if not config.BOT_TOKEN:
        raise RuntimeError(
            "Не задан токен бота. Установите переменную окружения BOT_TOKEN "
            "или впишите токен в config.py"
        )

    request = HTTPXRequest(
        connect_timeout=30.0,
        read_timeout=30.0,
        write_timeout=30.0,
        pool_timeout=30.0
    )

    application = (
        ApplicationBuilder()
        .token(config.BOT_TOKEN)
        .request(request)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(on_callback))

    return application


def main():
    application = build_application()
    logger.info("Бот запущен. Ожидание сообщений...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()