import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "7811367207:AAH39vjyrr3mqz1dvBmgr25WBf9GpGat8LI"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # pylint: disable=unused-argument
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # pylint: disable=unused-argument
    """Echo the user message."""
    user = update.effective_user
    my_text = update.message.text
    my_text ="Hello" + " " + user.mention_html()+"\n"+my_text
    await update.message.reply_html(my_text)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

    # Локальный веб-сервер
    application.run_webhook(
        listen="0.0.0.0",
        port=8080,
        url_path='webhook',
        webhook_url=f"https://7abc-212-30-36-154.ngrok-free.app/webhook"
    )

def add(a: int,b: int) -> int:
    return a+b;

z = add(5,9);
print(z);

if __name__ == "__main__":
    main()