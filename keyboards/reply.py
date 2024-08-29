from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О магазине'),
        ],
        [
            KeyboardButton(text='Варинты доставки'),
            KeyboardButton(text='Варианты оплаты'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?'
)

del_kbd = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text='Меню'),
    KeyboardButton(text='О магазине'),
    KeyboardButton(text='Варианты доставки'),
    KeyboardButton(text='Варианты оплаты'),
)
start_kb2.adjust(2, 2)


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text='Оставить отзыв'))


test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text='Отправить номер', request_contact=True),
            KeyboardButton(text='Отправить локацию', request_location=True)
        ]
    ],
    resize_keyboard=True
)

