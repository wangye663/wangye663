from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_API_TOKEN' with the API token obtained from BotFather
TOKEN = '6431056796:AAGqVBt44TA-r_ozQyMqBmTR9av_OBkv-Sc'

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello, I am your Telegram bot.')

def echo(update: Update, context: CallbackContext
