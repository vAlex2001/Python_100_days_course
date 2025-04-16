import requests
from twilio.rest import Client

TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_token"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_url = 'https://www.alphavantage.co/query'
stock_api_key = "9STWFU9463UPMCF3"

news_url = 'https://newsapi.org/v2/everything'
news_api_key = "49713e25ecc94d9eafd7e77452dff400"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
api_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': stock_api_key
}


# Get yesterday closing price.
response = requests.get(stock_url, params=api_params, verify=False)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday closing price.
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the absolute value of the difference between the two closing prices.
price_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

# Find the percentage difference between the two closing prices.
percentage_difference = (price_difference / float(day_before_yesterday_closing_price)) * 100 

# If the percentage difference is greater than 5% then print("Get News").
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if percentage_difference > 1:
    news_params = {
        "apiKey": news_api_key,
        "qIntitle": COMPANY_NAME,
    }
    news_response = requests.get(news_url, params=news_params, verify=False)
    articles = news_response.json()["articles"]
    
    first_three_articles = articles[:3]
    
    formatted_articles = [f"Headline{article['title']}. \nBrief: {article['description']}" for article in first_three_articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
        message = client.message.create(
        body = article,
        from_ = "sender_number",
        to = "receiver_number"
    )   



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

