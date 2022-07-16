from re import X
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import numpy as np
import json

# python scripts imports
from s_portofolioUpdate import getUpdatedPortofolio, getPortofolioPieChart
from s_historicPerfomance import getHistoricPortofolioChart, getHistoricDividends, getProfitabilityInformation, getBenchmarkInformation 
from s_dataManagement import getNewOrderCurrencyRate, ImportAnualDividends, getAnnualBenchmark

# ---------------------------------------------------------------------------------
# --------------------------------- CONFIGURATION ---------------------------------
# ---------------------------------------------------------------------------------
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS, needed to accept requests from VUE
CORS(app, resources={r'/*': {'origins': '*'}})

# instantiate flask sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slqite.db' #three /// make path relative
db = SQLAlchemy(app)

# ---------------------------------------------------------------------------------
# ----------------------------------- MODELS --------------------------------------
# ---------------------------------------------------------------------------------
class Company_Info(db.Model):
    __tablename__ = 'company_info'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), unique=True, nullable=False)
    MyTicker = db.Column(db.String(10), unique=True, nullable=False)
    SearchTicker = db.Column(db.String(10), unique=True, nullable=False)
    Currency = db.Column(db.String(10), unique=False, nullable=False)
    Country = db.Column(db.String(50), unique=False, nullable=False)
    Sector = db.Column(db.String(50), unique=False, nullable=False)
    SuperSector = db.Column(db.String(50), unique=False, nullable=False)

class Company_Dividend(db.Model):
    __tablename__ = 'company_dividend'

    id = db.Column(db.Integer, primary_key=True)
    MyTicker = db.Column(db.String(10), unique=True, nullable=False)
    CurrentDividend = db.Column(db.Float, unique=False, nullable=False)

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    OrderType = db.Column(db.String(5), unique=False, nullable=False)
    OrderDate = db.Column(db.DateTime, nullable=False)
    MyTicker = db.Column(db.String(10), unique=False, nullable=False)
    Amount = db.Column(db.Float, unique=False, nullable=False)
    Price = db.Column(db.Float, unique=False, nullable=False)
    PriceBaseCurrency = db.Column(db.Float, unique=False, nullable=False)
    Total = db.Column(db.Float, unique=False, nullable=False)
    TotalBaseCurrency = db.Column(db.Float, unique=False, nullable=False)

class Portofolio(db.Model):
    __tablename__='portofolio'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), unique=True, nullable=False)
    MyTicker = db.Column(db.String(10), unique=True, nullable=False)
    Country = db.Column(db.String(50), unique=False, nullable=False)
    Currency = db.Column(db.String(10), unique=False, nullable=False)
    Sector = db.Column(db.String(50), unique=False, nullable=False)
    SuperSector = db.Column(db.String(50), unique=False, nullable=False)
    Amount = db.Column(db.Float, unique=False, nullable=False)
    AveragePrice = db.Column(db.Float, unique=False, nullable=False)
    CurrentPrice = db.Column(db.Float, unique=False, nullable=False)
    DividendShare = db.Column(db.Float, unique=False, nullable=False)
    MarketValue_BaseCurrency = db.Column(db.Float, unique=False, nullable=False)
    Dividend_BaseCurrency = db.Column(db.Float, unique=False, nullable=False)

class HistoricPortofolio(db.Model):
    __tablename__='historicPortofolio'

    id = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.Integer, unique=True, nullable=False)
    Deposit = db.Column(db.Float, unique=False, nullable=False)
    Withdraw = db.Column(db.Float, unique=False, nullable=False)
    NetDeposit = db.Column(db.Float, unique=False, nullable=False)
    PortofolioVaue = db.Column(db.Float, unique=False, nullable=False)

class HistoricDividends(db.Model):
    __tablename__='historicDividends'

    id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.DateTime, nullable=False)
    MyTicker = db.Column(db.String(10), unique=False, nullable=False)
    Currency = db.Column(db.String(10), unique=False, nullable=False)
    Amount = db.Column(db.Float, unique=False, nullable=False)
    AmountEuro = db.Column(db.Float, unique=False, nullable=False)

class Benchmark(db.Model):
    __tablename__='benchmark'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, unique=True, nullable=False)
    DictFinancialData = db.Column(db.Text, unique=False, nullable=False)
    
# only run db.create_all() if ddbb is not yet created or need to create a new table
# db.create_all()

# ---------------------------------------------------------------------------------
# ----------------------------------- ROUTES --------------------------------------
# ---------------------------------------------------------------------------------

# --------------------------- PORTOFOLIO VIEW ---------------------------------------

# get CURRENT PORTOFOLIO DATA, ticker, current price, market value, etc. SEND TO "ViewPortofolio.vue"
@app.route('/getPortofolio', methods=['GET'])
def getPortofolio():

    PortofolioList=[]
    TickerList=[]
    MarketValueList=[]
    DividendList=[]
    for row in Portofolio.query.all():
        CompanyDict={
            'Name': row.Name,
            'MyTicker': row.MyTicker,
            'Country': row.Country,
            'Currency': row.Currency,
            'Sector': row.Sector,
            'SuperSector': row.SuperSector,
            'Amount': row.Amount,
            'AveragePrice': "{:.1f}".format(row.AveragePrice),
            'CurrentPrice': row.CurrentPrice,
            'DividendShare': row.DividendShare,
            'MarketValue (€)': "{:.1f} €".format(row.MarketValue_BaseCurrency),
            'Dividend (€)': "{:.1f} €".format(row.Dividend_BaseCurrency)
        }

        PortofolioList.append(CompanyDict)
        TickerList.append(row.MyTicker)
        MarketValueList.append(row.MarketValue_BaseCurrency)
        DividendList.append(row.Dividend_BaseCurrency)

    # get total dividends/year and current market value of the portofolio
    TotalDividends=0
    TotalMarketValue=0
    for company in PortofolioList:
       Dividend = float(company['Dividend (€)'].strip(' (€)'))
       MarketValue = float(company['MarketValue (€)'].strip(' (€)'))
       TotalDividends = TotalDividends + Dividend
       TotalMarketValue = TotalMarketValue + MarketValue
    
    Yield="{:.2f} %".format(TotalDividends/TotalMarketValue*100)
    TotalDividends = "{:>12,.1f} €/year".format(TotalDividends) # >12, = thousand comma separator; .1f = 1 decimal point separator
    TotalMarketValue = "{:>12,.1f} €".format(TotalMarketValue)

    data=[PortofolioList, TotalDividends,TotalMarketValue, Yield, TickerList, MarketValueList, DividendList]

    return jsonify(data)

# get PORTOFOLIO PIE CHARTS according user selection (radio button). SEND TO "ViewPortofolio.vue"
@app.route('/PortolioCharts', methods=['POST'])
def getPortofolioCharts():
    if request.method=='POST':
        # post data from vue request (returns de user selection of a Portofolio Charts radio button)
        postData=request.get_json()
        radioSelection=postData['data']

        # get all portofolio data
        data=Portofolio.query.all()

        # response to retur to client. returns data to update the Portofolio pie charts
        response=getPortofolioPieChart(data, radioSelection)

    return jsonify(response)

# --------------------------- HISTORIC PERFORMANCE VIEW -------------------------------------

# get HISTORIC DATA (portofolio and dividends). SEND TO "ViewHistoricPerformance.vue"
@app.route('/historicInformation', methods=['GET'])
def getHistoricData():
    HistoricPortofolio_table = HistoricPortofolio.query.all()
    HistoricDividend_table = HistoricDividends.query.all()

    PortofolioData = getHistoricPortofolioChart(HistoricPortofolio_table)
    DividendData = getHistoricDividends(HistoricDividend_table)
    ProfitabilityData = getProfitabilityInformation(HistoricPortofolio_table)

    YieldCost = (DividendData[3]/PortofolioData[5])*100
    YieldCost = "{:.1f} %".format(YieldCost)

    data=[PortofolioData, DividendData, YieldCost, ProfitabilityData]

    return jsonify(data)

# updates BENCHMARK CHART according to user selection. SEND TO "ViewHistoricPerformance.vue"
@app.route('/historicBenchmark', methods=['GET','POST'])
def getHistoricBenchmark():
   
    # get data from vue and assign postData received to python variables
    postData=request.get_json(force=True)

    # query ddbb table to get all benchmark data
    Benchmark_table = Benchmark.query.all()

    BenchamarkData = getBenchmarkInformation(postData, Benchmark_table)
   
    return jsonify(BenchamarkData)

# --------------------------- STOCK ANALSYIS VIEW -------------------------------------




# ---------------------------- DATA MANAGEMENT VIEW --------------------------------------------
# Add NEW COMPANY. GET DATA FROM "FormNewCompnay.vue"and adds it to the database (table Stock_General_Info_db). 
@app.route('/addNewCompany', methods=['GET', 'POST'])
def AddNewCompany():
    postData=request.get_json(force=True)

    NewCompany=Company_Info(
        Name=postData['CompanyName'], 
        MyTicker=postData['MyTicker'], 
        SearchTicker=postData['API_Ticker'],
        Currency=postData['Currency'],
        Country=postData['Country'],
        Sector=postData['Sector'],
        SuperSector=postData['Supersector']
    )

    NewCompanyDividend=Company_Dividend(
        MyTicker=postData['MyTicker'],
        CurrentDividend=0 
    )
    
    db.session.add(NewCompany)
    db.session.add(NewCompanyDividend)
    db.session.commit()
    
    return jsonify('data uploaded to database')

# Add NEW ORDER. GET DATA FROM "FormNewOrder.vue" and adds to the database.
@app.route('/postNewOrder', methods=['GET','POST'])
def getVueData():
    postData=request.get_json(force=True)
    Ticker=postData['Ticker']

    # call company_Info table to get the currency of the ticker. Then call script s_newOrder to return currenctyRate
    company = Company_Info.query.filter_by(MyTicker=Ticker).first()
    currency=company.Currency
    currencyRate=getNewOrderCurrencyRate(currency)
    
    # define new entry to the Order table
    NewOrder=Order(
       OrderType=postData['OrderType'],
       OrderDate=datetime.strptime(postData['Date'], '%Y-%m-%d'),
       MyTicker=postData['Ticker'],
       Amount=float(postData['Amount']),
       Price=float(postData['Price']),
       PriceBaseCurrency=float(postData['Price'])/currencyRate,
       Total=float(postData['Amount'])*float(postData['Price']),
       TotalBaseCurrency=float(postData['Amount'])*float(postData['Price'])/currencyRate
    )

    # save new order into ddbb
    db.session.add(NewOrder)
    db.session.commit()
    
    return jsonify('data uploaded to database')

# get ALL COMPANY TICKERS FROM ddbb
@app.route('/getTickers', methods=['GET', 'POST'])
def getTickers():

    CompanyList=Company_Info.query.all()

    tickerList=[]
    for company in CompanyList:
        tickerList.append(company.MyTicker)

    return jsonify(tickerList)

# UPDATE CURRENT PORTOFOLIO
@app.route('/updatePortoflio', methods=['GET', 'POST'])
def updateportofolio():

    # delete all rows from previous table
    Portofolio.query.delete()

    #get new data 
    CompanyInfo_table = Company_Info.query.all()
    Order_table = Order.query.all()
    Dividend_table = Company_Dividend.query.all()
    data=[CompanyInfo_table, Order_table, Dividend_table]
      
    UpdatedPortofolio_dict = getUpdatedPortofolio(data)
  
    for stock in UpdatedPortofolio_dict:
        UpdatedCompany=Portofolio(
            Name=UpdatedPortofolio_dict[stock]['Name'],
            MyTicker=UpdatedPortofolio_dict[stock]['Ticker'],
            Country=UpdatedPortofolio_dict[stock]['Country'],
            Currency=UpdatedPortofolio_dict[stock]['Currency'],
            Sector=UpdatedPortofolio_dict[stock]['Sector'],
            SuperSector=UpdatedPortofolio_dict[stock]['SuperSector'],
            Amount=UpdatedPortofolio_dict[stock]['Amount'],
            AveragePrice=UpdatedPortofolio_dict[stock]['Average price'],
            CurrentPrice=UpdatedPortofolio_dict[stock]['Current price'],
            DividendShare=UpdatedPortofolio_dict[stock]['DividendShare'],
            MarketValue_BaseCurrency=UpdatedPortofolio_dict[stock]['Total (€)'],
            Dividend_BaseCurrency =UpdatedPortofolio_dict[stock]['Dividend (€/year)']
        )

        # save new order into ddbb
        db.session.add(UpdatedCompany)
        db.session.commit()

    return jsonify('portofolio updated')

# add ANNUAL NAV. Get data from FormAddAnnualNAV.vue and adds it to the ddbb (HistoricPortofolio table)
@app.route('/AddAnnualNAV', methods=['GET', 'POST'])
def addAnnualNAV():
    # get data from post request (vue sends data)
    postData=request.get_json(force=True)

    Year = int(postData['Year'])
    Deposit = float(postData['Deposit'])
    Withdraw = float(postData['Withdraw'])
    PortofolioValue = float(postData['PortofolioValue'])
    NetDeposit = Deposit - Withdraw

    # Create new ddbb entry to store in HistoricPortofolio table
    AnnualNAV=HistoricPortofolio(
        Year = Year, 
        Deposit = Deposit, 
        Withdraw = Withdraw,
        NetDeposit = NetDeposit,
        PortofolioVaue = PortofolioValue
    )

    # save new order into ddbb
    db.session.add(AnnualNAV)
    db.session.commit()

    return jsonify('hola')

# Add NEW YEAR OF DIVIDENDS. Get data from FormImportAnualDividends.vue and adds it to the ddbb (table HistoricDividedns)
@app.route('/addAnualDividends', methods=['GET', 'POST'])
def addAnualDividends():
    # get data from post request (vue sends data)
    postData=request.get_json(force=True)

    # call python script located in s_dataManagement.py
    AnnualDividendList = ImportAnualDividends(postData)

    # stores returned data in sqlite ddbb
    for row in AnnualDividendList:
        NewAnualDividend=HistoricDividends(
            Date = row[0],
            MyTicker = row[1],
            Currency = row[2],
            Amount = row[3],
            AmountEuro = row[5]
        )

        db.session.add(NewAnualDividend)
        db.session.commit()

    return jsonify('Annual dividends added to database')

# Add NEW ANNUAL INDEX BENCHMARKS. Get data from FormAddBenchmarks.vue and adds it to the ddbb (table Benchmark)
@app.route('/addAnnualBenchmark', methods=['GET', 'POST'])
def addAnnualBenchmark():
    year=request.get_json(force=True)
    HistoricPortofolio_table = HistoricPortofolio.query.all()

    AnnualBenchmarks = getAnnualBenchmark(year, HistoricPortofolio_table)

    newBenchmark = Benchmark(
        year =year,
        DictFinancialData = json.dumps(AnnualBenchmarks)
    )

    db.session.add(newBenchmark)
    db.session.commit()

    return 'Benchmarks added to the database!'


# ----------------------------------- TEST route ------------------------------------
@app.route('/test', methods=['GET', 'POST'])
def test():

    return jsonify('hello')

# ---------------------------------------------------------------------------------
# ----------------------------------- APP.RUN ------------------------------------
# ---------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()