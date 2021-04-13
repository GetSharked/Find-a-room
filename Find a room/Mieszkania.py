from bs4 import BeautifulSoup
from requests import get


def parse_price(price):
    return price.replace(' ', '').replace('zł', '')

def parse_page(number):
    page = get(f'{URL}&page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')
    for offer in bs.find_all('div', class_='offer-wrapper'):
        footer = offer.find('td', class_='bottom-cell')
        title = offer.find('strong').get_text().strip()
        price = parse_price(offer.find('p', class_='price').get_text().strip())
        link = offer.find('a')
        print(title + ' CENA: ' + price)
        print(link['href'])

URL = 'https://www.olx.pl/nieruchomosci/stancje-pokoje/wroclaw/?search%5Bfilter_enum_roomsize%5D%5B0%5D=one'


for page in range(1, 26):
    parse_page(page)



