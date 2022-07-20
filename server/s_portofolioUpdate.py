import pandas as pd
import requests
import json

from s_getExchangeRates import getExchangeRates

def getUpdatedPortofolio(data):
    ## ----------------------------------------------------------------------------------------------------- ##
    ## --------------------------- IMPORTING DATA AND PREPARING INITIAL DF --------------------------------- ##
    ## ----------------------------------------------------------------------------------------------------- ##
    print('starting script')

    CompanyInfo_table=data[0]
    Order_table=data[1]
    Dividend_table=data[2]

    ## prepare CompanyInfo_df 
    Name=[company.Name for company in CompanyInfo_table]
    InfoTicker=[company.MyTicker for company in CompanyInfo_table]
    SearchTicker=[company.SearchTicker for company in CompanyInfo_table]
    Currency=[company.Currency for company in CompanyInfo_table]
    Country=[company.Country for company in CompanyInfo_table]
    Sector=[company.Sector for company in CompanyInfo_table]
    SuperSector=[company.SuperSector for company in CompanyInfo_table]
    CompanyInfo_dict={
        'Name':Name, 
        'Ticker':InfoTicker,
        'SearchTicker':SearchTicker,
        'Currency':Currency, 
        'Country':Country, 
        'Sector':Sector, 
        'SuperSector':SuperSector
    }

    df_CompanyInfo=pd.DataFrame(CompanyInfo_dict)
    df_CompanyInfo=df_CompanyInfo.set_index(['Ticker'])

    ## prepare Order_df
    OrderTicker=[order.MyTicker for order in Order_table]
    Amount=[order.Amount for order in Order_table]
    Total=[order.Total for order in Order_table]
    TotalBaseCurrency=[order.TotalBaseCurrency for order in Order_table]
    Order_dict={
        'Ticker':OrderTicker,
        'Amount':Amount,
        'Total':Total,
        'Total (€)':TotalBaseCurrency
    }
    
    df_Order=pd.DataFrame(Order_dict)
    df_Order=df_Order.set_index(['Ticker'])
    df_Order=df_Order.groupby('Ticker').sum() ## sum "Amount", "Total" & "Total (€)" with groupby
    df_Order=df_Order.loc[(df_Order!=0).any(axis=1)] ## drop rows with zeros

    ## prepare Dividend_df
    DividendTicker=[dividend.MyTicker for dividend in Dividend_table]
    DividendShare=[dividend.CurrentDividend for dividend in Dividend_table]
    Dividend_dict={
        'Ticker':DividendTicker,
        'DividendShare':DividendShare
    }
    
    df_dividend=pd.DataFrame(Dividend_dict)
    df_dividend=df_dividend.set_index(['Ticker'])

    ## merge df to df_portofolio
    df_portofolio = pd.merge(df_CompanyInfo, df_Order, on='Ticker')
    df_portofolio=pd.merge(df_portofolio,df_dividend, on='Ticker')

    ## ----------------------------------------------------------------------------------------------------- ##
    ## ---------------------------------- ADD COLUMNS TO df_portofolio ------------------------------------- ##
    ## ----------------------------------------------------------------------------------------------------- ##

    ## ------------------------------- add ['Average price'] column -------------------------------------------
    df_portofolio['Average price']=df_portofolio['Total']/df_portofolio['Amount']

    ## -------------------- add ['Current price'] column (call to Rapid Api) ----------------------------------
    def StockPriceMap(row):
        print('starting StockPriceMap function')
        print(row)
        url="https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/" + row

        headers = {
        'x-rapidapi-key': "f160d6aebamshae49215262502edp110b27jsn6f09ea528fcb",
        'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        response=json.loads(response.text) #returns a list of dictionaires, if only one ticker, a list with only one dictionary
        marketClose=response[0]['regularMarketPrice']

        return marketClose
    
    df_portofolio['Current price']=df_portofolio['SearchTicker'].apply(lambda row: StockPriceMap(row)) ## populate ['Current price'] column based on ['Search Ticker'] column applying StockPriceMap(row) function


    ## ----------------------- add ['CurrencyRate'] column (call to Rapid Api) -----------------------------------
    CureencyRate_dict=getExchangeRates()

    def CurrencyMap(row):
        if row=='EUR':
            return CureencyRate_dict['EUR']
        elif row=='USD':
            return CureencyRate_dict['USD']
        elif row=='GBP':
            return CureencyRate_dict['GBP']*100
        elif row=='HKD':
            return CureencyRate_dict['HKD']
        else:
            return 'missing currency'
    
    df_portofolio['CurrencyRate']=df_portofolio['Currency'].apply(lambda row: CurrencyMap(row)) ## populate CurrencyRate column based on Currency value column applying CurrencyMap(row) function

    # --------------------------- Add ['Total (€)'] and ['Dividend (€/year)'] columns ------------------------------------------
    df_portofolio['Total (€)']=df_portofolio['Amount']*df_portofolio['Current price']/df_portofolio['CurrencyRate']
    df_portofolio['Dividend (€/year)']=df_portofolio['Amount']*df_portofolio['DividendShare']/df_portofolio['CurrencyRate']

    ## ----------------------------------------------------------------------------------------------------- ##
    ## -------------------- REORGANIZE COLUMSN AND RETURN A JSON STRING TO app.py -------------------------- ##
    ## ----------------------------------------------------------------------------------------------------- ##  
    df_portofolio=df_portofolio.reset_index()
    df_portofolio=df_portofolio[[
        'Name',
        'Ticker',
        'Country',
        'Currency',
        'Sector',
        'SuperSector',
        'Amount',
        'Average price',
        'Current price',
        'DividendShare',
        'Total (€)',
        'Dividend (€/year)'
    ]]

    portofolio_dict=df_portofolio.to_dict('index')

    return portofolio_dict


def getUpdateDividends(CompanyInfo_table):

    tickerList = [data.SearchTicker for data in CompanyInfo_table]
    CountryList = [data.Country for data in CompanyInfo_table]

    MyDict = {
        'Ticker': tickerList,
        'Country': CountryList
    }

    df = pd.DataFrame(MyDict)

    ## -------------------- add ['Current price'] column (call to Rapid Api) ----------------------------------
    def CountryMap(row):
        if row == 'Spain':
            return 'ES'
        elif  row == 'USA':
            return 'US'
        elif row == 'Germany':
            return 'DE'
        elif row == 'France':
            return 'FR'
        elif row == 'Netherlands':
            return 'AU'
        elif  row == 'United Kingdom':
            return 'UK'
        else:
            return 'Emerging Markets'

    df['CountryMap']=df['Country'].apply(lambda row: CountryMap(row)) ## populate ['CountryMap'] column based on ['Country'] column applying CountryMap(row) function

    tickersES = df.loc[df['CountryMap'] == 'ES']
    listES = ",".join(tickersES['Ticker'].to_list())

    tickersUS = df.loc[df['CountryMap'] == 'US']
    listUS = ",".join(tickersUS['Ticker'].to_list())

    tickersDE = df.loc[df['CountryMap'] == 'DE']
    listDE = ",".join(tickersDE['Ticker'].to_list())

    tickersFR = df.loc[df['CountryMap'] == 'FR']
    listFR = ",".join(tickersFR['Ticker'].to_list())

    tickersAU = df.loc[df['CountryMap'] == 'AU']
    listAU = ",".join(tickersAU['Ticker'].to_list())

    tickersUK = df.loc[df['CountryMap'] == 'UK']
    listUK = ",".join(tickersUK['Ticker'].to_list())

    tickersEM = df.loc[df['CountryMap'] == 'EM']
    listEM = tickersEM['Ticker'].to_list()


    TickersCountryList = [listES, listUS, listDE, listFR, listAU, listUK]
 
    dividendRateList = []
    for tickers in TickersCountryList:
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

        querystring = {"region":"US","symbols":tickers}

        headers = {
            "X-RapidAPI-Key": "f160d6aebamshae49215262502edp110b27jsn6f09ea528fcb",
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)

        companiesDict = data['quoteResponse']['result']

        DividendRateCountryList = []
        for company in companiesDict:
            try:
                data = {
                    'ticker': company['symbol'].split(".",1)[0],
                    'dividendRate': company['dividendRate']
                }
            except:
                data = {
                    'ticker': company['symbol'].split(".",1)[0],
                    'dividendRate': 0
                }
               
            DividendRateCountryList.append(data)
        
        dividendRateList.append(DividendRateCountryList)
    
    return dividendRateList


def getPortofolioPieChart(data, radioSelection):

    PortofolioList=[]
    for row in data:
        CompanyDict={
            'MyTicker': row.MyTicker,
            'Country': row.Country,
            'Currency': row.Currency,
            'Sector': row.Sector,
            'SuperSector': row.SuperSector,
            'MarketValue (€)':row.MarketValue_BaseCurrency,
            'Dividend (€)': row.Dividend_BaseCurrency
        }

        PortofolioList.append(CompanyDict)

    df=pd.DataFrame.from_dict(PortofolioList)

    df=df.groupby([radioSelection]).sum()

    LabelList=df.index.values.tolist()
    MarketValueList=df['MarketValue (€)'].tolist()
    DividendList=df['Dividend (€)'].tolist()
    
    chartData=[LabelList, MarketValueList, DividendList]

    return chartData

