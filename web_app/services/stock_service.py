# web_app/services/stock_service.py

import requests
import json

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=abc123"
print(request_url)

response = requests.get(request_url)
print(type(response))
print(response.status_code)
print(type(response.text))

parsed_response = json.loads(response.text)
print(type(parsed_response))

latest_close = parsed_response["Time Series (Daily)"]["2020-02-25"]["4. close"]
print("LATEST CLOSING PRICE:", latest_close)
