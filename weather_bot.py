import aiogram
from src.weather import Weather
import asyncio
from src.functions_fot_weather_bot import register_handlers


async def main(BOT_KEY, WEATHER_KEY):
    bot = aiogram.Bot(BOT_KEY)
    bot["weather_connector"] = Weather(WEATHER_KEY)
    dp = aiogram.Dispatcher(bot)

    register_handlers(dp)

    print('bot running')
    await dp.start_polling()


file = open('botid_and_appid', 'r')
BOT_KEY, WEATHER_KEY = file.read().split()
asyncio.run(main(BOT_KEY, WEATHER_KEY))
