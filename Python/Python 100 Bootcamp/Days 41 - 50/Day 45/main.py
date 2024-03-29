from bs4 import BeautifulSoup
import lxml

with open ("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")

all_anchor_tags = soup.find_all(name="a")

heading = soup.find(name="h1",id="name")

name = soup.select_one("#name")

headings = soup.select(".heading")