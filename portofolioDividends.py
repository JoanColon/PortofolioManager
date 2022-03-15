import os
import pandas as pd

def getPortofolioDividends():
    # Get data
    cwd=os.getcwd()
    path=os.path.join(cwd,'data','AllDividends.csv')
    df=pd.read_csv(path)

    # Dataframe with dividends by Ticker
    dfTicker=df.loc[:,['Tickers','Amount_euro']]
    dfTicker=dfTicker.groupby(['Tickers']).sum()
    dfTicker=dfTicker.reset_index()
    DividendTicker=dfTicker.to_dict(orient='records')

    for x in DividendTicker:
        x['Amount_euro']="{:.1f} €".format(x['Amount_euro']) #format number to only 1 demcimal and €

    # Dataframe with dividends by year
    dfDate=df.loc[:,['Date','Amount_euro']]
    dfDate['Date']=pd.to_datetime(dfDate['Date'])
    dfDate=dfDate.groupby(dfDate.Date.dt.year).sum()
    dfDate=dfDate.reset_index()
    dfDate=dfDate.rename(columns={'Date':'Xaxis', 'Amount_euro':'Yaxis'}, errors='raise')
    DividendYear=dfDate.to_dict(orient='list')

    historicDividends=[DividendTicker, DividendYear]

    return historicDividends
