from flask import Flask
from telegram.ext import ApplicationBuilder

TOKEN = "7811367207:AAH39vjyrr3mqz1dvBmgr25WBf9GpGat8LI"
WEBHOOK_URL = "https://bot-git.fly.dev/webhook"

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Бот работает!"

if __name__ == "__main__":
    app.run(port=8080, debug=True, host="localhost")    

'''
async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    await application.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=WEBHOOK_URL,
        web_app=app,
    )
    application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

'''
