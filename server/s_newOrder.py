import requests
import json

def newOrder_rate(currency):    
    url = "https://fixer-fixer-currency-v1.p.rapidapi.com/latest" ## rapidApi Fixer Currency API

    querystring = {"base":"EUR","symbols":"EUR,USD,GBP,HKD"}

    headers = {
        "X-RapidAPI-Host": "fixer-fixer-currency-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "f160d6aebamshae49215262502edp110b27jsn6f09ea528fcb"
    }

    response_currency = requests.request("GET", url, headers=headers, params=querystring) ## response from rapidAPI (returns a text)
    response_currency=json.loads(response_currency.text) ## transforms rapidApi response (text) to a python dictionary

    CureencyRate_dict={
        'EUR':response_currency['rates']['EUR'],
        'USD':response_currency['rates']['USD'],
        'GBP':response_currency['rates']['GBP'],
        'HKD':response_currency['rates']['HKD'],
    }

    if currency=='EUR':
        return CureencyRate_dict['EUR']
    elif currency=='USD':
        return CureencyRate_dict['USD']
    elif currency=='GBP':
        return CureencyRate_dict['GBP']*100
    elif currency=='HKD':
        return CureencyRate_dict['HKD']
    else:
        return 'missing currency'