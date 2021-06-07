import logging
import settings
from handlers import (find_planet, greet_user, guess_number, send_shrek_picture,
                    user_coordinates, talk_to_me, check_user_photo)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def main():
    mybot = Updater(settings.API_KEY, 
    #request_kwargs=PROXY, 
    use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("planet", find_planet))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("quess", guess_number))
    dp.add_handler(CommandHandler("shrek", send_shrek_picture))
    dp.add_handler(MessageHandler(Filters.regex("^(Я вызываю Шрека)$"), send_shrek_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
