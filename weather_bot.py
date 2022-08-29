import asyncio
import aiogram
from src.weather import Weather
from src.functions_fot_weather_bot import start, location_from_city, location


async def main(BOT_KEY, WEATHER_KEY):
    bot = aiogram.Bot(BOT_KEY)
    bot.weather_conektor = Weather(WEATHER_KEY)
    dp = aiogram.Dispatcher(bot)

    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(location, content_types=['location'])
    dp.register_message_handler(location_from_city)

    print('bot running')
    await dp.start_polling()


file = open('botid_and_appid', 'r')
BOT_KEY, WEATHER_KEY = file.read().split()
asyncio.run(main(BOT_KEY, WEATHER_KEY))
