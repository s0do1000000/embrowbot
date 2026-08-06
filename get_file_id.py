import logging
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

TOKEN = "8582789594:AAEQBRo3D6DvWNF_bMLIpn7zOUmmwzAPszw"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    
    if msg.photo:
        # Берём последнее фото из массива (самое высокое разрешение)
        file_id = msg.photo[-1].file_id
        await msg.reply_text(f"PHOTO file_id:\n{file_id}")
        print(f"PHOTO file_id: {file_id}")
        
    elif msg.video:
        file_id = msg.video.file_id
        await msg.reply_text(f"VIDEO file_id:\n{file_id}")
        print(f"VIDEO file_id: {file_id}")

def main():
    print("Ожидаю медиафайлы (фото и видео) от вас в Telegram... (Ctrl+C для остановки)")
    app = Application.builder().token(TOKEN).build()
    
    # Обрабатываем и фото, и видео
    app.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, handle_media))
    
    app.run_polling()

if __name__ == "__main__":
    main()