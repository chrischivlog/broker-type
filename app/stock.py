import json
import requests
import schedule
import time
import datetime

def job():

    # import stock information for multiplining the value of stock
    stocks_file = "stocks.json"

    # Stock API URL: https://marketstack.com/documentation_v2
    api_key_file = "api_key.json"
    with open(api_key_file, 'r') as f:
        api_data = json.load(f)
        api_key = api_data['api_key'] 

    webhook_url = 'https://discord.com/api/webhooks/881954769193820170/ucJoZAWQkaU5hItHwqFDDh_W8Nls0Qr1LxEFx1MxomoyT8x1pRg9cIxbEyD7DzbFz4yl'

    api_request = requests.get('http://api.marketstack.com/v2/eod/latest?access_key='+ api_key +'&symbols=AAPL')
    api = json.loads(api_request.content)

    # all the results from API request
    close_price = api['data'][0]['close']

    # calculate the total value of stock
    with open(stocks_file, 'r') as f:
        stock_data = json.load(f)
        stock_name = stock_data['name']
        stock_amount = float(stock_data['amount'])
        total_value = close_price * stock_amount
        print(f"The total value of {stock_amount} shares of {stock_name} is: ${total_value:.2f}")



    #trigger the webhook on discord to show the price closed at stock
    data = {
        "content": "The stock closed at: " + str(total_value)
    }

    result = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

# scheduler to run every friday at 4pm
schedule.every().sunday.at("17:10").do(job)

while True:
    schedule.run_pending()
    print(datetime.datetime.now())
    time.sleep(1)
    
