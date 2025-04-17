from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import config
import handlears

TOKEN = config.get_token()

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", handlears.start))
    # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlears.handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
