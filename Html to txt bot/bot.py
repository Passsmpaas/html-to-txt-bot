import os
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# ENV load karo
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")      # future use agar user account login karna ho
API_HASH = os.getenv("API_HASH")  # future use agar telethon/pyrogram use karna ho
API_URL = os.getenv("API_URL")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        file = await update.message.document.get_file()
        file_content = requests.get(file.file_path).content

        response = requests.post(API_URL, files={"file": ("input.html", file_content)})
        data = response.json()

        text_output = data.get("text", "")[:5000]
        links_output = "\n".join(data.get("links", []))

        output = f"=== Extracted Text ===\n{text_output}\n\n=== Extracted Links ===\n{links_output}"

        with open("converted.txt", "w", encoding="utf-8") as f:
            f.write(output)

        await update.message.reply_document(
            document=open("converted.txt", "rb"),
            filename="converted.txt",
            caption="✅ HTML file converted to TXT"
        )

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    app.run_polling()

if __name__ == "__main__":
    main()
      
