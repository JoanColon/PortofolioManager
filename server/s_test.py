import requests
import json
from datetime import datetime



def BenchmarkData(year):
    # symbols:
    # 'SP500':'SXR8.DE',
    # 'STOXX50': 'EXW1.DE',
    # 'FTSE100': 'SXRW.DE'
    #  'IBEX35': 'XESP.DE'
    
    symbols = ['SXR8.DE', 'EXW1.DE', 'SXRW.DE', 'XESP.DE']


  # ------------------------- GET DATA FROM YAHOO FINANCE -----------------------------------------------------------------
    yearTWRList=[]
    for symbol in symbols:
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-chart"

        querystring = {"interval":"1mo","symbol":symbol,"range":"2y","region":'DE',"includePrePost":"false","useYfid":"true","includeAdjustedClose":"true","events":"capitalGain,div,split"}

        headers = {
            "X-RapidAPI-Key": "f160d6aebamshae49215262502edp110b27jsn6f09ea528fcb",
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)

        # ------------------------- GET  YEAR TIME WEIGHETED RETURN (ANNUAL RETURN) ------------------------------------------
        
        # get timestamp and transform it to datetime
        timestamp = result['chart']['result'][0]['timestamp']
        dates = [datetime.fromtimestamp(time).strftime('%d-%m-%Y') for time in timestamp ]


        # get adjusted close
        adjustedClose = result['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

        # dict
        adjustedCloseDict = {}
        for x in range(len(dates)):
            date = str(dates[x])
            adjustedCloseDict[date] = adjustedClose[x]

        initYear = year
        finalYear = year + 1

        initValue = adjustedCloseDict[f'01-01-{initYear}']
        finalValue = adjustedCloseDict[f'01-01-{finalYear}']

        yearTWR = ((finalValue - initValue)/(initValue + 0)) + 1

        yearTWRList.append(yearTWR)

    yearTWRdict = {
        year:{
            'SP500': yearTWRList[0],
            'STOXX50': yearTWRList[1],
            'FTSE100': yearTWRList[2],
            'IBEX35': yearTWRList[3]
        }
    }

    print(yearTWRdict)
    
    return yearTWRdict

BenchmarkData(2021)

