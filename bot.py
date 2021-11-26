from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, chataction
import qrcode

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
            [button3],
            [InlineKeyboardButton(text="Link", callback_data="qr")]
            ])
    )


def qr_command_handler(update, context):

    update.message.reply_text("Env")

    return INPUT_TEXT


def qr_callback_handler(update, context):

    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text="Enlace del bot /start"
)

    return INPUT_TEXT


if __name__ == "__main__":

    updater = Updater(token="2118043418:AAECCp0EIBqJaDgkfQeATEaSFn9YIpk9yF8", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler("qr", qr_command_handler),
            CallbackQueryHandler(pattern="qr", callback=qr_callback_handler)
        ],

        states={
            INPUT_TEXT: [MessageHandler(Filters.text, "")]
        },

        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()
