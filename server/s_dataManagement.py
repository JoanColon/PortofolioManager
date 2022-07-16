import pandas as pd

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

def getAnnualReturnAndDividendRate(historicData):
    #  function to be used to get the needed data (Annual Rate of Return & Dividend Rate) to populate the Benchmark table with portofolio data. 
    # The rest of the data (Annual benchmark index data) is directly filled by the user, but for the portofolio is calculated automatically

    # ----------------- PortofolioHistoricData. To Calculate Annual Rate of Return -----------------------------------
    PortofolioHistoricData = historicData[0]
    
    currentYear = PortofolioHistoricData[-1]
    previousYear = PortofolioHistoricData[-2]

    FinalValue = currentYear.PortofolioVaue
    InitialValue = previousYear.PortofolioVaue
    NetDeposit = currentYear.NetDeposit
    year = currentYear.Year

    # TWR formula: https://www.investopedia.com/terms/t/time-weightedror.asp, Net deposit at the beginning of the yera
    yearTWR = ((FinalValue - (InitialValue + NetDeposit))/(InitialValue + NetDeposit)) + 1

    # ---------------------------------- DividendHistoricData. To Calculate % dividend ------------------------------------
    DividendHistoricData = historicData[1]

    # prepre the dataframe from sqlite imported data
    Date=[data.Date for data in DividendHistoricData]
    MyTicker=[data.MyTicker for data in DividendHistoricData]
    Currency=[data.Currency for data in DividendHistoricData]
    Amount=[data.Amount for data in DividendHistoricData]
    AmountEuro=[data.AmountEuro for data in DividendHistoricData]
    HistoricDividentDict={
        'Date':Date,
        'MyTicker':MyTicker,
        'Currency': Currency,
        'Amount':Amount,
        'AmountEuro':AmountEuro
    }

    df=pd.DataFrame.from_dict(HistoricDividentDict)

    # Dataframe with dividends by year
    dfDate=df.loc[:,['Date','AmountEuro']]
    dfDate['Date']=pd.to_datetime(dfDate['Date'])
    dfDate=dfDate.groupby(dfDate.Date.dt.year).sum()
    dfDate=dfDate.reset_index()

    # use @ in query to use the variable year defined previously (in Annual Rate of Return)
    AnnualDividend = dfDate.query('Date == @year')['AmountEuro'].iloc[0]

    dividendRate = AnnualDividend/FinalValue

    data = [yearTWR, dividendRate ]

    return data