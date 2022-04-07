import requests
import json

#url from rapidApi to connect to yahoo finance - removed the last part (after /quote), needs the list of tickers at the end
url_init="https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/"

myList=['SAN.MC','MSFT','TEF.MC']
#final url to connect to rapid Api with all tickers to extract the data
for x in myList:
    url=url_init + x

    headers = {
        'x-rapidapi-key': "f160d6aebamshae49215262502edp110b27jsn6f09ea528fcb",
        'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    response=json.loads(response.text) #returns a list of dictionaires, if only one ticker, a list with only one dictionary
    marketClose=response[0]['regularMarketPrice']
    print(marketClose)