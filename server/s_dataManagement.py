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