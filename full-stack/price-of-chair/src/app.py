import requests
from bs4 import BeautifulSoup


request = requests.get("https://www.johnlewis.com/herman-miller-aeron-office-chair/p230630306")
content = request.content
soup = BeautifulSoup(content, "html.parser")
# <strong class="simpleNowPrice">£899.00</strong>
element = soup.find("strong", {"class": "simpleNowPrice"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 500.00:
    print("Buy the chair!")
    print("The current price is {}.".format(string_price))
else:
    print("don't buy the chair!")
    print("The current price is {}.".format(string_price))
