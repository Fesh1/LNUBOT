import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import ParseMode
import json
import datetime
import pytz
from settings.consts import TOKEN, password, faculties, admins_id
from parse_functions.parser import LNU_parser, faculty_getter
from data.database import session, User
import logging


Lviv_timezone = pytz.timezone('Europe/Minsk')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def send_message(user_id, images, text):
    if images:
        for img in images:
            bot.send_photo(user_id, photo=img, caption=text, parse_mode=ParseMode.HTML)
    else:
        bot.send_message(user_id, text=text, parse_mode=ParseMode.HTML)


def newsletter(context: CallbackContext):
    all_user = session.query(User).all()
    for user in all_user:
        user_id = user.chat_id
        faculty = user.faculty

        if faculty == 'all':
            print('work', newsletter.__name__)
            for fac in faculties:
                parser = LNU_parser(fac, newsletter.__name__)
                text = parser.clean()
                images = parser.img_extractor()
                send_message(user_id, images, text)
        else:
            parser = LNU_parser(faculty, newsletter.__name__)
            text = parser.clean()
            images = parser.img_extractor()
            send_message(user_id, images, text)

    del parser


def reminder(update: Updater, context: CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,
                     text='Бот буде надсилати вам актуальні новини на сайті факультету кожен день')
    context.job_queue.run_daily(newsletter,
                                datetime.time(hour=22, minute=30), context=update.message.chat_id)


def get_article_by_id(update: Updater, context: CallbackContext):
    chat_id = update.message.chat.id

    info = update.message.text.replace('/get_article ', '')
    info = info.split()

    parser = LNU_parser(info, get_article_by_id.__name__)

    text = parser.clean()
    print(text)
    images = parser.img_extractor()

    if images:
        for img in images:
            bot.send_photo(chat_id, photo=img, caption=text, parse_mode=ParseMode.HTML)
        del parser
    else:
        bot.send_message(chat_id, text=text, parse_mode=ParseMode.HTML)
    del parser


def get_employee(update: Updater, context: CallbackContext):
    # request from bot
    chat_id = update.message.chat.id
    info = update.message.text.replace('/get_employee', '')
    info = info.split()

    parser = LNU_parser(info, get_employee.__name__)
    text = parser.clean()
    images = parser.img_extractor()
    if images:
        for img in images:
            bot.send_photo(chat_id, photo=img, caption=text, parse_mode=ParseMode.HTML)
        del parser
    else:
        bot.send_message(chat_id, text=text, parse_mode=ParseMode.HTML)


def set_faculty(update: Updater, context: CallbackContext):
    chat_id = update.message.chat.id
    info = update.message.text.replace('/set_faculty', '').replace(' ', '')
    with open("data/chat_info.json", "r+") as IDs:
        data = json.load(IDs)
        if chat_id not in data['all_id']:
            update.message.reply_text("Спочаку потрібно активувати бота командою \start")
            pass
    try:
        faculty = faculty_getter(info)
    except:
        update.message.reply_text("такого факультету не існує!")

    session.query(User).filter(User.chat_id == chat_id).update({User.faculty: faculty})
    session.commit()


def start(update: Updater, context: CallbackContext):
    print('start work')
    chat_id = update.message.chat.id
    info = update.message.text.replace('/start password=', '').replace(' ', '')

    if info == password:
        admins_id.append(chat_id)
        session.query(User).filter(User.chat_id == chat_id).update({User.admin_right: True, User.faculty: 'all'})
        session.commit()
        update.message.reply_text('Привіт адмін')
    else:

        update.message.reply_text(
            "привіт! я – бот, який допоможе тобі знайти інформацію про потрібного викладача, а також буде надсилати"
            "інформаціюпро актуальні новина на твоєму факультеті, для цього тобі потрібно його вказати командою "
            "/set_faculty <назва факультету>, наприклад /set faculty фізичний")

    with open("data/chat_info.json", "r+") as IDs:
        data = json.load(IDs)
        if chat_id not in data['all_id']:
            data['all_id'] = data['all_id'] + [chat_id]
            IDs.seek(0)
            json.dump(data, IDs)
            if info == password:
                new_admin = User(chat_id=chat_id)
                session.add(new_admin)
                session.commit()
            else:
                new_user = User(chat_id=chat_id)
                session.add(new_user)
                session.commit()


if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)
    bot = telegram.Bot(token=TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('get_article', get_article_by_id))
    dp.add_handler(CommandHandler('get_employee', get_employee))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('set_faculty', set_faculty))
    dp.add_handler(CommandHandler('newsletter', newsletter))
    dp.add_handler(CommandHandler('reminder', reminder, pass_job_queue=True))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
