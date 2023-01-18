import os

import logging
import datetime
import time
import telebot
import sqlite3
from telebot import types
from telebot_calendar import Calendar, CallbackData, ENGLISH_LANGUAGE

from telebot.types import ReplyKeyboardRemove, CallbackQuery, Message
from typing import Type


from config import BOT_TOKEN
from functions.converter_function import converter_voice_msg
from functions.spotify_api import get_songs
from state_tree.about_section.contact_info import Contact_info
from state_tree.about_section.website import Website
from state_tree.base_state import BaseState
from state_tree.ffeel_tools.converter import Converter
from state_tree.make_an_order.calendar import Create_calendar
from state_tree.make_an_order.get_file_recording import GetFileRecording
from state_tree.make_an_order.get_file_session import GetFileSession
from state_tree.make_an_order.get_references import GetReferences
from state_tree.make_an_order.one_more_ref import One_more
from state_tree.about_section.our_playlist import MyPlaylist
from state_tree.make_an_order.ghostwriting_section import Ghostwriting
from state_tree.make_an_order.additional_info import AdditionalInfo
from state_tree.make_an_order.confirmed import Confirmed
from state_tree.make_an_order.deadline import Deadline
from state_tree.make_an_order.recording_section import Recording
from state_tree.make_an_order.session_musician_section import SessionMusician
from state_tree.question_answers.two import Two
from state_tree.start import Start, Authorization
from state_tree.ffeel_tools.reference import Reference
from state_tree.change_phone_number import Change_phone_number
from state_tree.ffeel_tools.reference_tempo import Reference_tempo

# Creating logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
log_format = '%(asctime)s | %(levelname)s: %(message)s'
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)

USER_STEP = {}  # keeping track of user's current state (key: user id, value: class Basestate)

ORDER_INFO = {}  # info about user's order (key: str, value: str)

SPOTIFY_LINK = ''  # user's link to a spotify playlist (used in FFeelTools "Підібрати референси")

REFERENCES = set()  # user's reference tracks for making order in FFeelTools "Трек під ключ")

FORWARD_FILE = []  # info required to forward user's file to me

MY_ID = 862438449  # my id in telegram

# creating telegram calendar
calendar = Calendar(language=ENGLISH_LANGUAGE)
calendar_1_callback = CallbackData("calendar_1", "action", "year", "month", "day")

# available bot commands (shown when user prints /help)
help_commands = {
    'start': 'Знайомство з ботом 🦾',
    'help': 'Дізнайся про всі доступні команди 🗣'}

#hideBoard = types.ReplyKeyboardRemove()


def listener(messages: list) -> None:
    """
    Logging all user's messages
    """
    for m in messages:
        if m.content_type == 'text':
            logger.info(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


# creating telegram bot
bot = telebot.TeleBot(BOT_TOKEN)
# starting a bot listener (for the 'listener' function)
bot.set_update_listener(listener)


def is_in_database(user_id: int) -> bool:
    """
    Checks if user is already in the client database
    """

    with sqlite3.connect("FFeelMusicClients.db") as connection:
        c = connection.cursor()
        authorization_status = c.execute("SELECT EXISTS(SELECT 1 FROM Clients WHERE Id=?)",
                                         (user_id,)).fetchone()

        return authorization_status == (1,)


def authorization(message: Message) -> bool:
    """
    Puts user's info into the client database (SQL3 LITE)
    """

    phone_number = message.text.replace(" ", "")

    if phone_number.startswith('+380') and len(phone_number) == 13 and phone_number[1:].isnumeric():
        params = (message.from_user.id, message.from_user.first_name,
                  message.from_user.username, phone_number)

        with sqlite3.connect("FFeelMusicClients.db") as connection:
            c = connection.cursor()
            c.execute(
                "INSERT OR IGNORE INTO Clients"
                "(Id, first_name, username, phone_number)"
                "VALUES (?,?,?,?)", params)

            bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
            time.sleep(1)

            bot.send_message(message.chat.id, 'Успішно зареєстровано ✅')

            return True

    return False


def update_phone_number(message: Message) -> bool:

    "Changes client's phone number in the database"

    phone_number = message.text.replace(" ", "")
    user_id = message.from_user.id

    if phone_number.startswith('+380') and len(phone_number) == 13 and phone_number[1:].isnumeric():
        with sqlite3.connect("FFeelMusicClients.db") as connection:
            c = connection.cursor()
            c.execute("UPDATE Clients SET phone_number=? WHERE Id=?", (phone_number, user_id,))

            bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
            time.sleep(1)

            bot.send_message(message.chat.id, 'Успішно змінено! ✅')
            return True

    return False


def store_spotify_link(message: Message) -> bool:
    """
    Stores user's link in the SPOTIFY_LINK variable
    """

    link = message.text

    if link.startswith('https://open.spotify.com/playlist/'):
        global SPOTIFY_LINK
        SPOTIFY_LINK = link

        return True

    return False


def send_references(message: Message) -> bool:
    """
    Sends tracks (artist - song title) filtered by tempo from a playlist given by user
    """

    tempo = message.text

    if tempo.isnumeric() and 65 < int(tempo) < 240:

        bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
        time.sleep(1)

        for artist, song in get_songs(SPOTIFY_LINK, message.text).items():
            bot.send_message(message.chat.id, f'{artist} - {song}')

        return True

    return False


def store_title(message: Message) -> bool:

    if message.content_type != 'text':
        return False

    current_state: BaseState = USER_STEP[message.chat.id]

    if isinstance(current_state, Recording):
        ORDER_INFO['Послуга📍'] = 'Запис партії'

    elif isinstance(current_state, Ghostwriting):
        ORDER_INFO['Послуга📍'] = 'Гоустрайтинг'

    elif isinstance(current_state, SessionMusician):
        ORDER_INFO['Послуга📍'] = 'Сесійний музикант'

    band_title = message.text
    ORDER_INFO['Назва✏️'] = band_title

    USER_STEP[message.chat.id] = USER_STEP[message.chat.id].process()

    return True


def store_references(message: Message) -> bool:
    USER_STEP[message.chat.id] = USER_STEP[message.chat.id].process()

    reference = message.text

    if reference.startswith('https://'):

        if len(REFERENCES) == 2:
            REFERENCES.add(reference)
            return True
        else:
            REFERENCES.add(reference)
            return False

    USER_STEP[message.chat.id] = GetReferences()


def store_deadline(date: str) -> bool:
    deadline = date
    ORDER_INFO['Дедлайн⏱'] = deadline

    return True


def store_add_info(message: Message) -> bool:
    info = message.text
    ORDER_INFO['Додаткова інформація🗒'] = info

    return True


def send_order(message: Message) -> bool:

    if message.text != 'FFeel':
        return False

    order = f'Замовлення від @{message.from_user.username} 🎹: \n\n'

    for key, value in ORDER_INFO.items():
        order += f"{key} - {value} \n\n"

    bot.send_message(MY_ID, order)

    if ORDER_INFO['Послуга📍'] == 'Запис партії':
        bot.forward_message(FORWARD_FILE[0], FORWARD_FILE[1],
                            FORWARD_FILE[2])

    elif ORDER_INFO['Послуга📍'] == 'Гоустрайтинг':

        for reference in REFERENCES:
            bot.send_message(MY_ID, reference)

    elif ORDER_INFO['Послуга📍'] == 'Сесійний музикант':
        bot.forward_message(FORWARD_FILE[0], FORWARD_FILE[1],
                            FORWARD_FILE[2])

    bot.send_message(message.chat.id, "Замовлення відправлено! ✅")

    return True


def make_calendar(message: Message) -> None:
    now = datetime.datetime.now()

    bot.send_message(
        message.chat.id,
        "Календар👇",
        reply_markup=calendar.create_calendar(
            name=calendar_1_callback.prefix,
            year=now.year,
            month=now.month,
        ),
    )


def send_studio_location(message: Message) -> bool:
    bot.send_location(message.chat.id, 50.62230637013628, 26.262728422743947)
    return True


def send_my_contact(message: Message) -> bool:
    bot.send_contact(message.chat.id, phone_number='+380979153382', first_name='Dima Philipchuk')
    USER_STEP[message.chat.id] = USER_STEP[message.chat.id].process()
    return True


def send_my_spotify_playlist(message: Message) -> bool:
    bot.send_photo(message.chat.id, photo=open("pictures/playlist_cover.jpg", 'rb'))

    bot.send_message(message.chat.id,
                     text="<a href='https://open.spotify.com/playlist/6Ud9RGICEhn84flFAfFeTM?si=c4a6827a19e34a3f'>"
                          "Перейти до плейлисту 🖱</a>",
                     parse_mode="HTML")

    USER_STEP[message.chat.id] = USER_STEP[message.chat.id].process()

    return True


def send_my_website(message: Message) -> bool:

    bot.send_message(message.chat.id,
                     text="<a href='http://project6565316.tilda.ws/'>Перейти до вебсайту ⌨️</a>",
                     parse_mode="HTML")

    USER_STEP[message.chat.id] = USER_STEP[message.chat.id].process()

    return True


@bot.callback_query_handler(
    func=lambda call: call.data.startswith(calendar_1_callback.prefix)
)
def callback_inline(call: CallbackQuery) -> None:

    logger.info(call.data)

    name, action, year, month, day = call.data.split(calendar_1_callback.sep)

    date = calendar.calendar_query_handler(
        bot=bot, call=call, name=name, action=action, year=year, month=month, day=day
    )

    if action == "DAY":

        bot.send_message(
            chat_id=call.from_user.id,
            text=f"Ти обрав {date.strftime('%d.%m.%Y')}",
            reply_markup=ReplyKeyboardRemove(),
        )

        user_date = date.strftime('%d.%m.%Y')

        logger.info(str(call.message.chat.first_name) + " [" + str(call.message.chat.id) + "]: " + user_date)

        store_deadline(user_date)

        USER_STEP[call.message.chat.id] = USER_STEP[call.message.chat.id].process(txt=call.data)
        markup_handler(call.message.chat.id)

    elif action == "CANCEL":
        bot.send_message(
            chat_id=call.from_user.id,
            text="Відміна ⛔️",
            reply_markup=ReplyKeyboardRemove(),
        )

        USER_STEP[call.message.chat.id] = Deadline()
        markup_handler(call.message.chat.id)


@bot.message_handler(commands=["start"])
def command_start(message: Message) -> None:
    USER_STEP[message.chat.id] = Start()

    current_state: BaseState = USER_STEP[message.chat.id]

    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)

    bot.send_message(message.chat.id, current_state.msg, parse_mode="HTML")

    if is_in_database(message.from_user.id):
        USER_STEP[message.chat.id] = USER_STEP[message.chat.id].process(authorized=True)
    else:
        USER_STEP[message.chat.id] = USER_STEP[message.chat.id].process()

    markup_handler(message.chat.id)


@bot.message_handler(commands=['help'])
def command_help(message: Message) -> None:
    help_text = "Тобі доступні наступні команди: \n\n"

    for key in help_commands:
        help_text += "/" + key + ": "
        help_text += help_commands[key] + "\n"

    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(message.chat.id, help_text)


def markup_handler(chat_id: int) -> None:

    current_state: BaseState = USER_STEP.get(chat_id, Start())
    markup = types.InlineKeyboardMarkup()

    for button_msg, button_cmd in current_state.buttons:
        markup.add(types.InlineKeyboardButton(text=button_msg, callback_data=button_cmd))

    bot.send_message(chat_id, current_state.msg, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: CallbackQuery) -> None:
    actions = {Two: send_studio_location, Create_calendar: make_calendar,
               Contact_info: send_my_contact, MyPlaylist: send_my_spotify_playlist,
               Website: send_my_website, BaseState: None

               }

    current_state: BaseState = USER_STEP.get(call.message.chat.id, Start())

    for button_msg, button_cmd in current_state.buttons:
        if button_cmd == call.data:
            logger.info(str(call.message.chat.first_name) + " [" + str(call.message.chat.id) + "]: " + button_msg)
            bot.send_message(call.message.chat.id, button_msg)

    new_state: BaseState = current_state.process(txt=call.data)

    USER_STEP[call.message.chat.id] = new_state

    action = actions.get(type(new_state))

    if action:
        action(call.message)
    else:
        pass

    markup_handler(call.message.chat.id)


@bot.message_handler(content_types=['voice'])
def voice_processing(message: Message) -> None:
    current_state: BaseState = USER_STEP[message.chat.id]

    if type(current_state) != Converter:

        markup_handler(message.chat.id)

    else:

        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open('voice_message.m4a', 'wb') as new_file:
            new_file.write(downloaded_file)

        converted = converter_voice_msg("voice_message.m4a")
        os.remove("voice_message.m4a")

        with open(converted, 'rb') as audio:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(2)
            bot.send_audio(message.chat.id, audio=audio)

        os.remove(converted)

        USER_STEP[message.chat.id] = USER_STEP[message.chat.id].process()
        markup_handler(message.chat.id)


# noinspection PyTypeChecker
@bot.message_handler(content_types=["text"])
def message_handler(message: Message) -> None:

    actions_dict = {Reference: store_spotify_link, Change_phone_number: update_phone_number,
                    Reference_tempo: send_references, Authorization: authorization,

                    Recording: store_title,
                    AdditionalInfo: store_add_info, Confirmed: send_order,

                    Ghostwriting: store_title, GetReferences: store_references,
                    One_more: store_references,

                    SessionMusician: store_title, Create_calendar: make_calendar

                    }

    current_state: BaseState = USER_STEP[message.chat.id]
    action = actions_dict.get(type(current_state))

    if action:

        if not action(message):

            markup_handler(message.chat.id)

        else:

            new_state: BaseState = current_state.process(txt=message.text, authorized=True)
            USER_STEP[message.chat.id] = new_state
            markup_handler(message.chat.id)
    else:

        markup_handler(message.chat.id)


@bot.message_handler(content_types=["audio", "document"])
def file_handler(message: Message) -> None:

    current_state: BaseState = USER_STEP[message.chat.id]

    if type(current_state) != GetFileRecording and type(current_state) != GetFileSession:

        markup_handler(message.chat.id)

    else:

        logger.info(str(message.chat.first_name) + " [" + str(message.chat.id) + "]: " + '"Файл відправлено"')

        FORWARD_FILE.extend([862438449, message.chat.id, message.id])
        USER_STEP[message.chat.id] = USER_STEP[message.chat.id].process()
        markup_handler(message.chat.id)


@bot.message_handler(content_types=["sticker"])
def sticker(message: Message) -> None:
    logger.info(str(message.chat.first_name) + " [" + str(message.chat.id) + "]: " + '"Відправлено стікер"')
    bot.send_message(message.chat.id, "Ти відправив стікер 😁")
    markup_handler(message.chat.id)


@bot.message_handler(content_types=["photo", "video", "video_note", "location", "contact", "animation"])
def invalid_input(message: Type[telebot.types.Message]) -> None:
    logger.warning(str(message.chat.first_name) + " [" + str(message.chat.id) + "]: " +
                   '"Відправлено неправильний тип данних"')
    bot.send_message(message.chat.id, "Я не розумію 😁")
    markup_handler(message.chat.id)


if __name__ == '__main__':
    bot.infinity_polling()
