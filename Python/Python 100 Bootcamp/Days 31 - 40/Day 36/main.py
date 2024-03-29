import requests
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#first stock api key - jumiduss
# api_key_stock = "5804A6RW5PCBDTZZ"
#second stock api key - yospikydog
#### API Limit Hit
api_key_stock = "K990X4KXWTLT9RIG"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={api_key_stock}"
request = requests.get(url)
url_stock_data = request.json()
with open("stock_dict.json", "w") as file:
    json.dump(url_stock_data,file)
with open("stock_dict.json","r") as file:
    url_stock_data = json.load(file)
    
stock_data = url_stock_data["Time Series (Daily)"]
closing_data = [stock_data[day]["4. close"] for day in stock_data]

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

api_key_news = "232ff7f104844722a925ff328c695c90"

def get_news(date):
#     global api_key_news
#     url = ('https://newsapi.org/v2/everything?'
#        f'q={COMPANY_NAME}&'
#        f'from={date}&'
#        'sortBy=popularity&'
#        f'apiKey={api_key_news}')
    
#     request =  requests.get(url)
#     url_news_data = request.json()
    # with open("news_dict.json", "w") as file:
    #     json.dump(url_news_data,file)
    with open("news_dict.json","r") as file:
        url_news_data = json.load(file)
    
    return url_news_data['articles'][0:4]
    # news_data = url_news_data[]
    
    
# Step 1
list_len = len(closing_data)
day_difference = [
    list(stock_data.keys())[i+1] for i in range(list_len - 1) if (
        (((float(closing_data[i+1]) - float(closing_data[i])) / float(closing_data[i])) * 100) > 5
    )]

article_set = {}
for date in day_difference: 
    if int(date[5:7]) < 5:
        article_set = get_news(date)

split_articles = {key:article for key,article in enumerate(article_set)}

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    # Twilio is broken, printing to console instead
article_details_dict = {key:{"title":value["title"],"description":value["description"]} for (key,value) in split_articles.items()}

for (key,value) in article_details_dict.items():
    print(f"{STOCK}:\nArticle:{key}\n{value['title']}\n{value['description']}")
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""