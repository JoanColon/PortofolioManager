from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# python scripts imports
from portofolio import getInvestingData
from portofolioDividends import getPortofolioDividends

# ---------------------------------------------------------------------------------
# --------------------------------- CONFIGURATION ---------------------------------
# ---------------------------------------------------------------------------------
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
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
    Currency = db.Column(db.String(10), unique=True, nullable=False)
    Country = db.Column(db.String(10), unique=True, nullable=False)
    Sector = db.Column(db.String(10), unique=True, nullable=False)
    SuperSector = db.Column(db.String(10), unique=True, nullable=False)

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    OrderType = db.Column(db.String(5), unique=False, nullable=False)
    OrderDate = db.Column(db.String(50))
    MyTicker = db.Column(db.String(10), unique=False, nullable=False)
    Amount = db.Column(db.Float, unique=False, nullable=False)
    Price = db.Column(db.Float, unique=False, nullable=False)
    PriceBaseCurrency = db.Column(db.Float, unique=False, nullable=False)
    Total = db.Column(db.Float, unique=False, nullable=False)
    TotalBaseCurrency = db.Column(db.Float, unique=False, nullable=False)

# only run db.create_all() if ddbb is not yet created
db.create_all()

# ---------------------------------------------------------------------------------
# ----------------------------------- ROUTES --------------------------------------
# ---------------------------------------------------------------------------------

# get current portofolio data, ticker, current price, market value, etc. SEND TO "ViewPortofolio.vue"
@app.route('/getPortofolio', methods=['GET'])
def getPortofolio():
    portofolio=getInvestingData() #function imported from portofolio.py file

    return jsonify(portofolio)

# get historic dividend data. SEND TO "ViewDividends.vue"
@app.route('/historicDividends', methods=['GET'])
def getHisotoricDividends():
    historicDividends=getPortofolioDividends() #funciton imported from portofolioDivindeds.py

    return jsonify(historicDividends)

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
    
    db.session.add(NewCompany)
    db.session.commit()
    
    return jsonify('data uploaded to database')

# Add NEW ORDER. GET DATA FROM "ViewPortofolio.vue" and adds to the database.
@app.route('/postNewOrder', methods=['GET','POST'])
def getVueData():
    postData=request.get_json(force=True)

    NewOrder=Order(
       OrderType=postData['OrderType'],
       OrderDate=postData['Date'],
       Ticker=postData['Ticker'],
       Amount=postData['Amount'],
       Price=postData['Price'],
       PriceBaseCurrency=100,
       Total=float(postData['Amount'])*float(postData['Price']),
       TotalBaseCurrency=float(postData['Amount'])*100,
    )

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

# ---------------------------------------------------------------------------------
# ----------------------------------- APP.RUN -------------------------------------
# ---------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()