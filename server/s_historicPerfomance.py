import pandas as pd

def getHistoricPortofolioChart(HistoricPortofolio_table):
    # prepre the dataframe from sqlite imported data
    Year=[data.Year for data in HistoricPortofolio_table]
    Deposit=[data.Deposit for data in HistoricPortofolio_table]
    Withdraw=[data.Withdraw for data in HistoricPortofolio_table]
    NetDeposit=[data.NetDeposit for data in HistoricPortofolio_table]
    PortofolioValue=[data.PortofolioVaue for data in HistoricPortofolio_table]
    HistoricPortofolioDict={
        'Year':Year,
        'Deposit':Deposit,
        'Withdraw': Withdraw,
        'NetDeposit':NetDeposit,
        'PortofolioValue':PortofolioValue,
    }

    df=pd.DataFrame.from_dict(HistoricPortofolioDict)

    # create new columns
    df['NetDepositCumsum']=df['NetDeposit'].cumsum()
    df['PortofolioCumsum']=df['PortofolioValue'].cumsum()

    # chart data
    YearList=df['Year'].tolist()
    NetDepositList=df['NetDeposit'].tolist()
    NetDepositCumsumList=df['NetDepositCumsum'].tolist()
    PortofolioValueList=df['PortofolioValue'].tolist()

    # total added funds, for card data
    TotalNetDepositYieldCost=NetDepositCumsumList[-1]
    TotalNetDeposit="{:>12,.1f} €".format(NetDepositCumsumList[-1])

    PortofolioChartData=[YearList, NetDepositList, NetDepositCumsumList, PortofolioValueList,TotalNetDeposit, TotalNetDepositYieldCost]

    return PortofolioChartData

def getHistoricDividends(HistoricDividend_table):
    # prepre the dataframe from sqlite imported data
    Date=[data.Date for data in HistoricDividend_table]
    MyTicker=[data.MyTicker for data in HistoricDividend_table]
    Currency=[data.Currency for data in HistoricDividend_table]
    Amount=[data.Amount for data in HistoricDividend_table]
    AmountEuro=[data.AmountEuro for data in HistoricDividend_table]
    HistoricDividentDict={
        'Date':Date,
        'MyTicker':MyTicker,
        'Currency': Currency,
        'Amount':Amount,
        'AmountEuro':AmountEuro
    }

    df=pd.DataFrame.from_dict(HistoricDividentDict)

    # TotalDividendsReceived
    TotalDividends = "{:>12,.1f} €".format(df['AmountEuro'].sum())

    # Dataframe with dividends by Ticker
    dfTicker=df.loc[:,['MyTicker','AmountEuro']]
    dfTicker=dfTicker.groupby(['MyTicker']).sum()
    dfTicker=dfTicker.reset_index()
    DividendTicker=dfTicker.to_dict(orient='records')

    for x in DividendTicker:
        x['AmountEuro']="{:.1f} €".format(x['AmountEuro']) #format number to only 1 demcimal and €

    # Dataframe with dividends by year
    dfDate=df.loc[:,['Date','AmountEuro']]
    dfDate['Date']=pd.to_datetime(dfDate['Date'])
    dfDate=dfDate.groupby(dfDate.Date.dt.year).sum()
    dfDate=dfDate.reset_index()
    dfDate=dfDate.rename(columns={'Date':'Xaxis', 'AmountEuro':'Yaxis'}, errors='raise')
    DividendYear=dfDate.to_dict(orient='list')

    # Total Amount of Dividends received
    DividendsLastYear = DividendYear['Yaxis'][-1]

    historicDividends=[DividendTicker, DividendYear, TotalDividends, DividendsLastYear]

    return historicDividends

