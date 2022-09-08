import aiohttp


class Weather():
    API = "https://api.openweathermap.org/data/2.5"

    def __init__(self, key):
        self.key = key

    async def request(self, **params):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    "https://api.openweathermap.org/data/2.5/weather",
                    params={
                        'APPID': self.key,
                        'units': 'metric',
                        'lang': 'ru',
                        **params
                    }
            ) as asin:
                return await asin.json()

    async def weather_by_locashon(self, longitude: float, latitude: float):
        return await self.request(lon=longitude, lat=latitude)

    async def weather_by_city(self, city):
        return await self.request(q=city)


if __name__ == '__main__':
    file = open('../botid_and_appid', 'r')
    BOT_KEY, WEATHER_KEY = file.read().split()
    weather_object = Weather(WEATHER_KEY)
    a = weather_object.weather_by_locashon(longitude=37.4711, latitude=55.9401)
    b = weather_object.weather_by_city(city='ghfdhfhtgfjyfjyf')
    d = weather_object.weather_by_city(city='Деревня сенькино-секерино')
    c = weather_object.weather_by_city(city='Сенькино-секерино')
    print(b, d, c)
    pass
