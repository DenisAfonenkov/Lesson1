from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )



def greet_user(bot, update):
	text ='вызван /старт'
	print(text)
	update.message.reply_text(text)





def main():
    updater = Updater("398322537:AAHNfWQFDlJc65729pY5jwis1gHyVzNep6E")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    updater.start_polling()
    updater.idle()

def talk_to_me(bot, update):
	user_text = update.message.text
	print(user_text)
	update.message.reply_text(user_text)

main()
