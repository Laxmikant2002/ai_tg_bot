import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from pymongo import MongoClient
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Use /trend <industry> to get industry trends or /ask <your question> to ask a digital marketing question.')

def trend(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        update.message.reply_text('Please specify an industry.')
        return

    industry = context.args[0]
    client = MongoClient(Config.DATABASE_URL)
    db = client.trends_db
    collection = db.trends
    trend_data = collection.find_one({"industry": industry})

    if trend_data:
        response = f"Trends for {industry}:\nCPC: {trend_data['cpc']}\nCTR: {trend_data['ctr']}\nConversion Rate: {trend_data['conversion_rate']}"
    else:
        response = f"No data available for {industry}."

    update.message.reply_text(response)

def ask(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        update.message.reply_text('Please ask a question.')
        return

    question = ' '.join(context.args)
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=150
    )

    answer = response.choices[0].text.strip()
    update.message.reply_text(answer)

def main() -> None:
    updater = Updater(Config.TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("trend", trend))
    dispatcher.add_handler(CommandHandler("ask", ask))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()