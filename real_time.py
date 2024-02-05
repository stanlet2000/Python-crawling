import time

import requests
from bs4 import BeautifulSoup

stock_url = "https://finance.yahoo.com/world-indices/"

# print(table.text)
target = '^GSPC'

def print_price(target, check_response=False):
    response = requests.get(stock_url)
    if check_response:
        print(response)

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_ = 'W(100%)')

    table_content = table.find('tbody')

    indices = table_content.find_all('tr')
    for i in indices:
        if target == i.find('td').text:
            indice = i

    elements = indice.find_all('td')
    for element in elements:
        if element['aria-label'] == 'Last Price':
            print(element.text)
    print(indice.text)



if __name__ == '__main__':
    timestep = 10

    for i in range(timestep):
    # while True:
        time.sleep(5)
        print_price(target, check_response=True)