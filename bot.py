import os
import telegram
from telegram.ext import *
from telegram import *
from requests import *

INPUT_TEXT = 0

randomImageText = "Random Image"

randomPImageUrl = "https://picsum.photos/200/300"

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
    
    button4 = ([KeyboardButton("Random Image")]
    reply_markup=ReplyKeyboardMarkup(buttons))

    update.message.reply_text(
            text='"PHOTO Y NOMBRE DE LA BOTONERA SI DESEA"',
            reply_markup=InlineKeyboardMarkup([
                [button1],
                [button2],
                [button3]
                ])
        )

def messageHandler(update: Update, context: CallbackContext):
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
    dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

    updater.start_polling()
    updater.idle()
