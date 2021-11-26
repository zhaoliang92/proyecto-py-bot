from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, chataction

INPUT_TEXT = 0


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


if __name__ == "__main__":

    updater = Updater(token="2118043418:AAECCp0EIBqJaDgkfQeATEaSFn9YIpk9yF8", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()
