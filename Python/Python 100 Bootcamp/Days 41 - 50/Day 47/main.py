import requests
import lxml
from bs4 import BeautifulSoup
import json

link="https://www.amazon.com/LG-65-Inch-Processor-AI-Powered-OLED65C3PUA/dp/B0BVXDPZP3"

r = requests.get(
    link,
    headers={
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept-Language":"en-US,en;q=0.5"
    }
)
soup = BeautifulSoup(r.content,"lxml")
price_tag = soup.find("span",class_="a-price a-text-price")
price = price_tag.find("span",class_="a-offscreen")
print(price.text)