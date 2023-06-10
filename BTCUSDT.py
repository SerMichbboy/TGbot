# парсинг цены на
import requests


def scrape():
    response = requests.get(URL)
    response_json = response.json()
    return int(response_json["USD"]["last"])


URL = 'https://blockchain.info/ru/ticker'


def return_price():
    last_price = None
    while True:
        latest_price = scrape()
        if latest_price != last_price:
            last_price = latest_price
        return last_price
