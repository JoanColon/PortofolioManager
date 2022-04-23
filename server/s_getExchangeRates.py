import requests
import json

def getExchangeRates():
    ## first rapidApi API to test, if not work try the except route 
    try:   
        url = "https://exchangerate-api.p.rapidapi.com/rapid/latest/EUR"

        headers = {
            "X-RapidAPI-Host": "exchangerate-api.p.rapidapi.com",
            "X-RapidAPI-Key": "f160d6aebamshae49215262502edp110b27jsn6f09ea528fcb"
        }

        response_currency = requests.request("GET", url, headers=headers)
        response_currency=json.loads(response_currency.text) ## transforms rapidApi response (text) to a python dictionary
    
        CurrencyRate_dict={
            'EUR':response_currency['rates']['EUR'],
            'USD':response_currency['rates']['USD'],
            'GBP':response_currency['rates']['GBP'],
            'HKD':response_currency['rates']['HKD'],
        }

        print(CurrencyRate_dict)

        return CurrencyRate_dict

    ## second rapidApi call in case the first one is not working
    except: 
        url = "https://fixer-fixer-currency-v1.p.rapidapi.com/latest" ## rapidApi Fixer Currency API
        querystring = {"base":"EUR","symbols":"EUR,USD,GBP,HKD"}
        
        headers = {
            "X-RapidAPI-Host": "fixer-fixer-currency-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "f160d6aebamshae49215262502edp110b27jsn6f09ea528fcb"
            }
        
        response_currency = requests.request("GET", url, headers=headers, params=querystring) ## response from rapidAPI (returns a text)
        response_currency=json.loads(response_currency.text) ## transforms rapidApi response (text) to a python dictionary


        CurrencyRate_dict={
        'EUR':response_currency['rates']['EUR'],
        'USD':response_currency['rates']['USD'],
        'GBP':response_currency['rates']['GBP'],
        'HKD':response_currency['rates']['HKD'],
        }

        return CurrencyRate_dict
