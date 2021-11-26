import os
import telegram
from telegram.ext import *
from telegram import *
from requests import *

randomPeopleText = "Random Person"
randomImageText = "Random Image"

randomPeopleUrl = "https://"
randomPImageUrl = "https://"

likes = 0
dislikes = 0

allowedUsernames = ["medkurin"]

def startCommand(update, context):
    buttons = [[KeyboardButton("Random Image")], [KeyboardButton(randomPeopleText)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot!",
    reply_markup=ReplyKeyboardMarkup(buttons))

def messageHandler(update, context):
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

        buttons = [[InlineKeyboardButton("!", callback_data="like")], 
        [InlineKeyboardButton("?", callback_data="dislike")]]
        context.bot.send_message(chat_id=update.effective_chat.id, 
        reply_markup=InlineKeyboardButton(buttons), text="Did you like the image?")

def queryHandler(update, context):
    query = update.callback_query.data
    update.callback_query.answer()

    global likes, dislikes

    if "likes" in query:
        likes +=1

    if "dislikes" in query:
        dislikes +=1

    print(f"likes => {likes} and dislikes => {dislikes}")


if __name__ == "__main__":

    token = os.environ['TOKEN']

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", startCommand))
    dp.add_handler(MessageHandler(Filters.text, messageHandler))
    dp.add_handler(CallbackQueryHandler(queryHandler))
    
    updater.start_polling()
    updater.idle()
