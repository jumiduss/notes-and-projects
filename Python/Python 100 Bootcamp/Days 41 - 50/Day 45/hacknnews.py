from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
site_text = response.text
soup = BeautifulSoup(site_text,'lxml')

article_tag = soup.find_all(name="span", class_="titleline")
for story_title in article_tag:
    title_alone = story_title.find(name="a")
    print(title_alone.text)

# her way 
# score_list = soup.find_all(class_="score")
# scores = [score,getText for score in soup.find_all()name="span", class="title"]


score_list = soup.find_all(class_="score")
for score in score_list:
    print(score.text)