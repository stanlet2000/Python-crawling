import time

import requests
from bs4 import BeautifulSoup

stock_url = "https://finance.yahoo.com/world-indices/"

response = requests.get(stock_url)

print(response)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', class_ = 'W(100%)')

table_content = table.find('tbody')
# print(table.text)
target = '^GSPC'

indices = table_content.find_all('tr')

for i in indices:
    if target == i.find('td').text:
        indice = i

print(indice.text)
