settings = {
    "binance_keys":{
        "api_key":"< api-key >",
        "secret_key":"< secret-key >",
    },
    "telegram_token":"< telegram-token >",
    "user_alerts_limit":20,
    "user_tickers_limit":10
}
commands_description ={
    'help':
"""
*Общая информация*
Crypto Price Alerts - бот для создания уведомлений о ценах криптовалют

Поддерживаемые биржи: Binance(Список бирж будет расширяться)

Разработчик: @rommeltrader

*Синтаксис команд*

Спот пары записываются через "/": 
ETH/USDT, BTC/BUSD
Фьючерсные пары записываются полностью без разделителей:
ETHUSDT, BTCBUSD
Цена уведомления указыватся через точку: 3000.00
Регистр названия тикера неважен: Eth/usdt, BTCUSDT

*Доступные команды* 

/add - добавление нового уведомления

В качестве параметров выступают название тикера, цена и комментарий (необязательно)
Пример:
/add ETHUSDT 3000.00 Пробой уровня


/remove  - удаление уведомление(я)
В качестве параметра могут выступать название тикера и его цена, только название тикера или слово "all"
При названии тикера и его цене удалится только конкретное активное уведомление.
При только названии тикера удалятся все активные уведомления на этом тикере.
При слове "all" удалятся все активные уведомления.
Примеры:
/remove ETHUSDT 3000.00
Бот удалит уведомление по названию тикера и цене.
/remove ETHUSDT
Бот удалит все активные уведомления на тикере ETHUSDT
/remove all
Бот удалит все активные уведомления

/show - вывод активных уведомлений
В качестве параметра могут выступать название тикера или слово "all"
Пример:
/show all
Бот пришлет список всех активных уведомлений на всех тикерах
/show ETHUSDT
Бот пришлет список всех активных уведомлений на тикере ETHUSDT""",
    
    'start':'Добро пожаловать в бота Crypto Price Alerts. Для получения информации и списка команд введите /help',
}
errors = {
    'invalid_command':'Ошибка: Команда введена некорректно. Для получения инструкции введите /help',
    'invalid_ticker':'Ошибка: Указанный тикер отсутвует на поддерживаемых биржах или введен некорректно. Спот пары записываются через "/". Фьючерсные пары записываются без разделителей',
    'limit': 'Ошибка: У вас превышен лимит активных уведомлений или тикеров: максимально %s уведомлений на %s различных тикеров. используйте команду remove, чтобы удалить уведомления' %(settings['user_alerts_limit'],settings['user_tickers_limit']),
    'no_alerts_for_ticker':'У вас нет активных уведомлений на этот тикер (или тикер введен некорректно и отсутвует на поддерживаемых биржах)',
    'no_alerts':'У вас нет активных уведомлений',
    'no_alerts_for_ticker_and_price':'У вас нет такого уведомления',
    'invalid_price':'Ошибка: цена активации уведомления должна быть больше 0 и меньше 10 000 000',
    'unknown_command':'Неизвестная команда. Для получения списка команд введите /help'
    
}