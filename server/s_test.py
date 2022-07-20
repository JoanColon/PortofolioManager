import requests
import json
from datetime import datetime

tickersUS = "KO,PM,MSFT"
tickersES = "SAN.MC, ACS.MC"

tickersList = [tickersUS, tickersES]

for tickers in tickersList:
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region":"US","symbols":tickers}

    headers = {
        "X-RapidAPI-Key": "f160d6aebamshae49215262502edp110b27jsn6f09ea528fcb",
        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    companiesDict = data['quoteResponse']['result']

    DividendRateList = []
    for company in companiesDict:
        try:
            data = {
                'ticker': company['symbol'],
                'dividendRate': company['dividendRate']
            }
        except:
            data = {
                'ticker': company['symbol'],
                'dividendRate': 0
            }

        
        DividendRateList.append(data)

    print(DividendRateList)


