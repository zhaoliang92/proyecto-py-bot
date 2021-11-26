import os
import telegram
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, chataction

INPUT_TEXT = 0

randomPeopleText = "Random Person"
randomImageText = "Random Image"

randomPeopleUrl = "https://"
randomPImageUrl = "https://"

allowedUsernames = ["medkurin"]


def start(update, context):

    button1 = InlineKeyboardButton(
        text="Nombre canal o grupo",
        url="https://www.canal-o-grupo-de-telegram.com"
    )

    button2 = InlineKeyboardButton(
        text="Nombre canal o grupo",
        url="https://www.canal-o-grupo-de-telegram.com"
    )

    button3 = InlineKeyboardButton(
        text="Unete a la botonera",
        url="https://t.me/cheng_zhi"
    )

    update.message.reply_text(
            text='"PHOTO Y NOMBRE DE LA BOTONERA SI DESEA"',
            reply_markup=InlineKeyboardMarkup([
                [button1],
                [button2],
                [button3]
                ])
        )

def messageHandler(update: Update, context: CallbackContext):
    if update.effective_chat.username not in allowedUsernames:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You ar not allowed to use this bot")
        return
    if randomPeopleText in update.message.text:
        image = get(randomPeopleUrl).content
    if randomImageText in update.message.text:
        image = get(randomPImageUrl).content

    if image:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto
        (image, caption="")])


if __name__ == "__main__":

    token = os.environ['TOKEN']

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()
