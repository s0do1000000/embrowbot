# -*- coding: utf-8 -*-
"""
WSGI-приложение для запуска бота через Webhook (для PythonAnywhere Free).

ПОЧЕМУ ТАК:
PythonAnywhere на бесплатном тарифе не поддерживает постоянно работающие
процессы в фоне (long polling из bot.py умирает, когда закрывается консоль).
Зато бесплатный тариф ПОСТОЯННО держит живым Web-приложение (WSGI) — сайт
вида https://<youraccount>.pythonanywhere.com. Поэтому вместо long polling
бот принимает обновления от Telegram через HTTP-вебхук: каждый входящий
POST-запрос от Telegram превращается в Update и передаётся в те же
обработчики, что использует bot.py при обычном polling-запуске.

НАСТРОЙКА (один раз):

1) На вкладке "Web" -> раздел "Code" -> "Source code" укажите путь к папке
   проекта, например:
       /home/s0do1000000/embrowbot

2) На вкладке "Web" -> раздел "Code" -> "WSGI configuration file" — откройте
   этот файл (ссылка вида /var/www/s0do1000000_pythonanywhere_com_wsgi.py)
   и ЗАМЕНИТЕ ВСЁ ЕГО СОДЕРЖИМОЕ на:

       import sys
       path = '/home/s0do1000000/embrowbot'
       if path not in sys.path:
           sys.path.insert(0, path)

       from wsgi_bot import application

3) На вкладке "Web" убедитесь, что установлен Flask (если PythonAnywhere
   спросит про virtualenv — используйте тот, куда установлен
   requirements.txt этого проекта; либо просто выполните в Bash-консоли
   PythonAnywhere: pip3.11 install --user flask python-telegram-bot).

4) Нажмите зелёную кнопку "Reload s0do1000000.pythonanywhere.com" на
   вкладке Web.

5) Один раз пропишите Telegram, куда слать обновления — откройте в
   браузере (заменив ВАШ_ТОКЕН на реальный токен бота из BOT_TOKEN,
   в обоих местах одинаково):

   https://api.telegram.org/botВАШ_ТОКЕН/setWebhook?url=https://s0do1000000.pythonanywhere.com/webhook/ВАШ_ТОКЕН

   В ответ должно прийти {"ok":true,"result":true,"description":"Webhook was set"}.

   Проверить текущий статус вебхука можно так:
   https://api.telegram.org/botВАШ_ТОКЕН/getWebhookInfo

После этого просто пишите боту /start в Telegram — сообщения будут
приходить в виде вебхуков на ваш сайт, и process_update будет обрабатывать
их так же, как раньше при polling.

ВАЖНО: пока используется вебхук, обычный "python bot.py" (long polling)
запускать НЕ нужно — Telegram разрешает только один способ получения
обновлений одновременно (или webhook, или getUpdates/polling).
"""

import asyncio
import logging

from flask import Flask, request
from telegram import Update

import config
from bot import build_application

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

flask_app = Flask(__name__)

# Application строится один раз при старте процесса (при загрузке модуля).
telegram_app = build_application()


async def _process_update(update_data: dict):
    """
    Инициализирует приложение (initialize) на время обработки одного
    апдейта и корректно завершает (shutdown) после — это чуть медленнее,
    чем держать один долгоживущий event loop, зато надёжно работает в
    синхронной WSGI-модели PythonAnywhere вне зависимости от того,
    сколько потоков/процессов обрабатывают запросы.
    """
    async with telegram_app:
        update = Update.de_json(update_data, telegram_app.bot)
        await telegram_app.process_update(update)


# Токен в пути — простая защита: посторонний, не знающий токен бота,
# не сможет слать сюда поддельные "обновления".
@flask_app.route(f"/webhook/{config.BOT_TOKEN}", methods=["POST"])
def webhook():
    try:
        update_data = request.get_json(force=True)
        asyncio.run(_process_update(update_data))
    except Exception:
        logger.exception("Ошибка при обработке вебхука")
    return "OK"


@flask_app.route("/")
def index():
    return "Bot is running (webhook mode)!"


# PythonAnywhere (и WSGI-стандарт в целом) ожидает в модуле переменную
# с именем "application".
application = flask_app
