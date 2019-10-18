### Скріпт для відправки повідомлень про погоду у вказаному місті в телеграм

Опис скріптів:       
* ```RESULT_EXAMPLE.png``` - скрін роботи скріпта ```bot.py```;
* ```api_cofig.py``` - основні константи: токени, базові url, словник для певних міст;        
* ```weather_data.py``` - функція ```get_weather()``` для отримання інформації про погоду в місті;
* ```bot.py``` - комунікація із телеграмом: запустити скріпт, щоб відіслати повідомлення.
* ```bot_webhook.py``` - намагання щось зробити через flask i webhook (додаткові налаштування в ```readme_for_webhook.txt```), один раз навіть працювало;

Тестовий бот: *ArturWeatherForCityUkraineBot*.

Як працювати:
* відправити одне із міст: lviv, kyiv, rivne, chernivtsi, poltava;
* запустити запустити ```bot.py```
