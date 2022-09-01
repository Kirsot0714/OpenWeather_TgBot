from .text_localisation import TEXT
from aiogram import types  # для указание типов


def napravlenie_vetra(danie):
    yn = ((danie['wind']['deg'] + 22.5) % 360) // 45  # уравнение направления
    yn = int(yn)
    return TEXT[yn]


async def start(message):
    # Клавиатура с кнопкой запроса локации
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text=TEXT["Button_text_1"], request_location=True)
    keyboard.add(button_geo)
    await message.answer(TEXT["Start_message"], reply_markup=keyboard)


async def location_from_city(message: types.Message):
    pogoda = message.bot.get("weather_connector").weather_by_city(city=message.text)
    if 'message' not in pogoda:
        shablon = TEXT["weather_message"]
        await message.answer(
            text=shablon.format(pogoda, napravlenie_vetra(pogoda),
                                TEXT[pogoda['weather'][0]['description']]),
            parse_mode='HTML')
    else:
        await message.answer(
            text=TEXT["soobshenie_1"],
            parse_mode='HTML')


async def location(message: types.Message):
    if message.location is not None:
        shablon = TEXT["weather_message"]
        danie = message.location
        data = message.bot.get("weather_connector").weather_by_locashon(longitude=danie.longitude,
                                                                        latitude=danie.latitude)
        await message.answer(
            text=shablon.format(data, napravlenie_vetra(data), TEXT[data['weather'][0]['description']]),
            parse_mode='HTML')


def register_handlers(dp):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(location, content_types=['location'])
    dp.register_message_handler(location_from_city)
