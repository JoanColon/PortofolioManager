import requests
import pandas as pd
import json
from datetime import datetime

from s_getExchangeRates import getExchangeRates

def getNewOrderCurrencyRate(currency):
    CurrencyRate_dict=getExchangeRates()

    currencyRate=CurrencyRate_dict[currency]

    return currencyRate

def ImportAnualDividends(postData):
    # rename data send from client
    currencyDict=postData[0]
    csvData=postData[1]
    Separator=postData[2]

    # csv send in text format, code to transform text into the initial dataframe
    SplitCSV=csvData.splitlines( )

    dfList=[]
    for x in SplitCSV:
        x=x.split(Separator)
        Currency=x[2]
        Date=x[3]
        MyTicker=x[4].split('(')[0]
        Amount=x[5]
        NewEntry=[Date, MyTicker, Currency, Amount]
        dfList.append(NewEntry)
        print(dfList)
    
    df=pd.DataFrame(dfList)
    newHeader=df.iloc[0] # get first row to be used as headers
    df=df[1:] # get all rows minues the firstrow (headers)
    df.columns=newHeader # set the header names
    df.rename(columns={'Description':'MyTicker'}, inplace=True)

    # Work with df to get final working df
    df['Date']=pd.to_datetime(df['Date'])
    df['Amount']=df['Amount'].astype(float)

    def getExchangeRate(rowCurrency):
        if rowCurrency=='EUR':
            return float(currencyDict['EUR'])
        elif rowCurrency=='USD':
            return float(currencyDict['USD'])
        elif rowCurrency=='GBP':
            return float(currencyDict['GBP'])
        elif rowCurrency=='HKD':
            return float(currencyDict['HKD'])
        else:
            return 1
    
    df['ExchangeRate']=df['Currency'].apply(lambda rowCurrency: getExchangeRate(rowCurrency))
    df['AmountEuro']=df['Amount']/df['ExchangeRate']

    # Transforms de dataframe into a list of list... easier to loop and add into the sqlite database
    AnnualDividendList = df.values.tolist() 

    return AnnualDividendList

def getAnnualBenchmark(year, HistoricPortofolio_table):
    # symbols:
    # 'SP500':'SXR8.DE',
    # 'STOXX50': 'EXW1.DE',
    # 'FTSE100': 'SXRW.DE'
    # 'IBEX35': 'XESP.DE'
    
    symbols = ['SXR8.DE', 'EXW1.DE', 'SXRW.DE', 'XESP.DE']

    #------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------ GET BENCHMARK TWR ----------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------------
    yearTWRList=[]
    for symbol in symbols:
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-chart"

        querystring = {"interval":"1mo","symbol":symbol,"range":"10y","region":'DE',"includePrePost":"false","useYfid":"true","includeAdjustedClose":"true","events":"capitalGain,div,split"}

        headers = {
            "X-RapidAPI-Key": "f160d6aebamshae49215262502edp110b27jsn6f09ea528fcb",
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)
      
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
   
    #------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------ GET PORTOFOLIO TWR --------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------------
    
    # Code taken from -> s_historicPerfomance.py -> getProfitabilityInformation()

    YearList=[data.Year for data in HistoricPortofolio_table]
    NetDepositList=[data.NetDeposit for data in HistoricPortofolio_table]
    FinalValueList=[data.PortofolioVaue for data in HistoricPortofolio_table]
    
    InitialValueList = [0] # to prevent a division by 0 in year 1
    for x in FinalValueList[:-1]:
        InitialValueList.append(x)

    Year_List=[]
    TWR_List=[]
    for LoopYear in YearList: 
        n = LoopYear - YearList[0]

        # TWR formula: https://www.investopedia.com/terms/t/time-weightedror.asp, Net deposit at the beginning of the yera
        yearTWR = ((FinalValueList[n] - (InitialValueList[n] + NetDepositList[n]))/(InitialValueList[n] + NetDepositList[n])) + 1

        Year_List.append(LoopYear)
        TWR_List.append(yearTWR)

    Year_List=Year_List[1:]
    TWR_List = TWR_List[1:] # Portofolio started Dec '13, calculations will start from 2014 (remove 2013 data, first element of the list)

    PortofolioTWR_Dict={}
    for x in range(len(Year_List)):
        key = str(Year_List[x])
        value = TWR_List[x]

        PortofolioTWR_Dict[key]=value
    
    #------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------ CREATE THE FINAL TWR DICT TO SEND TO DDBB-----------------------------------
    #------------------------------------------------------------------------------------------------------------------------
    yearTWRdict = {
        'S&P500': yearTWRList[0],
        'STOXX50': yearTWRList[1],
        'FTSE100': yearTWRList[2],
        'IBEX35': yearTWRList[3],
        'Portofolio':PortofolioTWR_Dict[str(year)]
    }

    return yearTWRdict
