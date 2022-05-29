import pandas as pd

def getHistoricPortofolioChart(HistoricPortofolio_table):
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
    df['NetDepositCumsum']=df['NetDeposit'].cumsum()
    df['PortofolioCumsum']=df['PortofolioValue'].cumsum()

    # chart data
    YearList=df['Year'].tolist()
    NetDepositList=df['NetDeposit'].tolist()
    NetDepositCumsumList=df['NetDepositCumsum'].tolist()
    PortofolioValueList=df['PortofolioValue'].tolist()

    # total added funds, for card data
    TotalNetDeposit="{:>12,.1f} €".format(NetDepositCumsumList[-1])

    PortofolioChartData=[YearList, NetDepositList, NetDepositCumsumList, PortofolioValueList,TotalNetDeposit]

    return PortofolioChartData