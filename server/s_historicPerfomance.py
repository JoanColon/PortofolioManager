import json
import pandas as pd
import numpy as np
import numpy_financial as npf
from scipy.stats import gmean

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

def getProfitabilityInformation(HistoricPortofolio_table):
    # ---------------------------------------------------------------------------------------------------------------
    # ------------------------------- prepare the data from sqlite imported data -------------------------------
    # ---------------------------------------------------------------------------------------------------------------
    YearList=[data.Year for data in HistoricPortofolio_table]
    NetDepositList=[data.NetDeposit for data in HistoricPortofolio_table]
    FinalValueList=[data.PortofolioVaue for data in HistoricPortofolio_table]
  
    # ---------------------------------------------------------------------------------------------------------------
    # ---------------------------------------- Total Return calculation -----------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------
    PortofolioValue = FinalValueList[-1]
    NetDeposit = np.sum(NetDepositList)
    
    TotalReturnEuro = PortofolioValue - NetDeposit
    TotalReturnPercentage = ((PortofolioValue - NetDeposit) / NetDeposit) * 100

    # ---------------------------------------------------------------------------------------------------------------
    # ---------------------------------------- TWR & TWRR calculation -----------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------
    InitialValueList = [0] # to prevent a division by 0 in year 1
    for x in FinalValueList[:-1]:
        InitialValueList.append(x)

    Year_List=[]
    TWR_List=[]
    for year in YearList:
        n = year - YearList[0]

        # TWR formula: https://www.investopedia.com/terms/t/time-weightedror.asp, Net deposit at the beginning of the yera
        yearTWR = ((FinalValueList[n] - (InitialValueList[n] + NetDepositList[n]))/(InitialValueList[n] + NetDepositList[n])) + 1

        Year_List.append(year)
        TWR_List.append(yearTWR)

    TWR_List = TWR_List[1:] # Portofolio started Dec '13, calculations will start from 2014 (remove 2013 data, first element of the list)

    TWRvalue = (np.cumprod(TWR_List)[-1] - 1) * 100 # Time Weighted Return (using the cumulative product formula)
    TWRRvalue = (gmean(TWR_List) - 1) * 100 #Time Weigthed Rate of Return (using the geometric mean formula)

    # ---------------------------------------------------------------------------------------------------------------
    # -------------------------------------------- MWRR calculation -------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------
    
    # https://www.investopedia.com/terms/m/money-weighted-return.asp, Cash flow added at the beginning of the year 

    CashFlows = [CashFlow * -1 for CashFlow in NetDepositList]
    CashFlows.append(FinalValueList[-1])
    MWRRvalue = npf.irr(CashFlows) * 100

    # ---------------------------------------------------------------------------------------------------------------    
    # ------------------------------------ values to send to app.py -------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------
    TotalReturnEuros =  "{:,.1f} €".format(TotalReturnEuro)
    TotalReturnPercentage = "{:.1f} %".format(TotalReturnPercentage)
    TotalWeightedReturn = "{:.1f} %".format(TWRvalue)
    TotalWeightedRateReturn = "{:.1f} %".format(TWRRvalue)
    MoneyWeigthedRateReturn="{:.1f} %".format(MWRRvalue)

    data=[TotalReturnEuros, TotalReturnPercentage, TotalWeightedReturn, TotalWeightedRateReturn, MoneyWeigthedRateReturn]

    return data

def getBenchmarkInformation(postData, Benchmark_table):
    years = int(postData[0])
    SelectedBenchmarks = postData[1]

    # get data from only the necessary number of years (e.g., if years = 5, get the benchmark data from the last 5 years)
    Benchmark_table = Benchmark_table[-years:]

    # # create the list of benchmark data to return based on user seleciton, Benchmark Index to show and number of years
    yearList = [benchmark.year for benchmark in Benchmark_table]
    yearsCAGR = len(yearList)
    lastYear = yearList[-1] + 1
    yearList.append(lastYear)

    dataList = [json.loads(benchmark.DictFinancialData) for benchmark in Benchmark_table]

    sp500 = [TWRvalue['S&P500'] for TWRvalue in dataList]
    stoxx50 = [TWRvalue['STOXX50'] for TWRvalue in dataList]
    ftse100 = [TWRvalue['FTSE100'] for TWRvalue in dataList]
    Ibex35TR = [TWRvalue['IBEX35'] for TWRvalue in dataList]
    Portofolio = [TWRvalue['Portofolio'] for TWRvalue in dataList]

    OrganizedBenchmarks = {
        'sp500': sp500,
        'stoxx50': stoxx50,
        'ftse100': ftse100,
        'Ibex35TR': Ibex35TR,
        'Portofolio': Portofolio
    }


    # get chart Data for selected ticker
    initialInvestment = 10000.0
    FinalChartData = []
    BenchmarkKeyData = []
    for benchmark in SelectedBenchmarks:
        benchmarkData = OrganizedBenchmarks[benchmark]
        benchmarkDataList = list(np.cumprod(benchmarkData) * initialInvestment)
        benchmarkDataList.insert(0, initialInvestment)

        finalValue = benchmarkDataList[-1]
        CAGR_value = (finalValue/initialInvestment)**(1/yearsCAGR) - 1
        finalValueFormat = "{:,.1f}€".format(finalValue)
        CAGR_valueFormat = "{:.1%}".format(CAGR_value)

        ChartData = {benchmark:{'xAxis':yearList, 'yAxis':benchmarkDataList}}
        keyData = {benchmark:{'final Value': finalValueFormat, 'CAGR': CAGR_valueFormat}}
        FinalChartData.append(ChartData)
        BenchmarkKeyData.append(keyData)
          
    data = [FinalChartData, BenchmarkKeyData]
   
    return data

