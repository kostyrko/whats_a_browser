__author__ = 'jslvtr'

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/black/p4201464")
soup = BeautifulSoup(r.content, "html.parser")
element = soup.find("p", {"class":"price price--large"})
string_value = element.text.strip() #"£129.00"

price = float(string_value[1:])

if price < 100:
    print("Buy the chair!")
elif price == 100:
    print("Buy at your own peril!")
else:
    print("Definitely don't buy.")

# <p class="price price--large">£129.00</p>
