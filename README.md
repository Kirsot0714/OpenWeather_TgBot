# OpenWeather_TgBot
 OpenWeather_TgBot это тренировочный телеграм бот для изучения работы с API. Бот умеет выдавать погоду по координатам или городу которые отправил пользователь. 

**Использованные библиотек:**
- Aiogram
- Asincio

**Откуда брать ключи, куда их вводить:**

Для начала надо зарегистрировать своего бота в Telegram. В строке поиска вводите BotFather, заходите в него и пишите **/newbot**, затем пишите имя своего бота, к примеру "FirstBot". Затем напишите имя пользователя которое должно заканчиваться на bot, типа "my_bot" или "telegram_bot". Все, ключ бота есть. Теперь надо подключить сервис погоды. Я использую OpenWeather. Сперва надо зарегистрироваться в OpenWeather, когда зарегистрировались, жмёте на вкладку пользователя и выбираете пункт "My API keys" и в колонке Key находится ваш ключ. Ключ сервиса погоды готов, теперь у нас есть оба ключа и нам нужно вставить их в программу. В файле "botid_and_appid" в первой строчке мы пишем ключ бота, а во второй, ключ сервиса погоды.

Все ключи подключены, можно запускать бота.

**Опыт который я извлёк из работы над ботом:**

В первую очередь я научился создавать ботов и работать с ними.Во вторых я научился создавать асинхронные функции и брать информацию с сайтов.
