import time

import requests
from bs4 import BeautifulSoup

stock_url = "https://tw.stock.yahoo.com"


def print_price(check_response=False):
    response = requests.get(stock_url)
    if check_response:
        print(response)

    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', class_="Fw(600) Fz(40px) Lh(1) D(f) Ai(c) C($c-trend-down)")
    print(price.text)



if __name__ == '__main__':
    timestep = 20

    for i in range(timestep):
    # while True:
        time.sleep(10)
        print_price(check_response=True)