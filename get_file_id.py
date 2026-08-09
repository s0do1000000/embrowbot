# -*- coding: utf-8 -*-
"""
Служебный скрипт: помогает получить постоянный file_id для видео.

Как пользоваться:
1. Запустите: python get_file_id.py
2. В Telegram откройте своего бота и отправьте ему видео файлом
   (как видео, не как файл-документ) — то самое, длинное (171 МБ),
   через приложение Telegram это можно сделать даже с большим файлом,
   лимит на ЗАГРУЗКУ в Telegram — 2 ГБ, ограничение 50 МБ действует
   только на ОТПРАВКУ ботом через API.
3. В консоли появится file_id — скопируйте его в config.py
   (VIDEO_ABOUT_FILE_ID или VIDEO_LESSON_FILE_ID).
4. Остановите скрипт (Ctrl+C) и запускайте обычный bot.py.
"""

import logging

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

import config

logging.basicConfig(level=logging.INFO)


async def on_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    if video:
        print("\n=== FILE_ID ВИДЕО ===")
        print(video.file_id)
        print("======================\n")
        await update.message.reply_text(f"file_id:\n{video.file_id}")


def main():
    app = Application.builder().token(config.BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.VIDEO, on_video))
    print("Ожидаю видео от вас в Telegram... (Ctrl+C для остановки)")
    app.run_polling()


if __name__ == "__main__":
    main()
