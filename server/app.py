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
class Stock_General_Info_db(db.Model):
    __tablename__ = 'stock_general_info_db'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), unique=True, nullable=False)
    MyTicker = db.Column(db.String(10), unique=True, nullable=False)
    SearchTicker = db.Column(db.String(10), unique=True, nullable=False)
    Currency = db.Column(db.String(10), unique=True, nullable=False)
    Country = db.Column(db.String(10), unique=True, nullable=False)
    Sector = db.Column(db.String(10), unique=True, nullable=False)
    SuperSector = db.Column(db.String(10), unique=True, nullable=False)

# only run db.create_all() if ddbb is not yet created
# db.create_all()

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

# Add NEW ORDER. Get data from form and adds to the database. GET DATA FROM "ViewPortofolio.vue"
@app.route('/postNewOrder', methods=['GET','POST'])
def getVueData():
    postData=request.get_json(force=True)
    print(postData)
    
    return jsonify('data uploaded to database')

# Add NEW COMPANY. GET DATA FROM "FormNewCompnay.vue"and adds it to the database (table Stock_General_Info_db). 
@app.route('/addNewCompany', methods=['GET', 'POST'])
def AddNewCompany():
    postData=request.get_json(force=True)

    NewCompany=Stock_General_Info_db(
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

    print(postData['CompanyName'])
    
    return jsonify('data uploaded to database')

# ---------------------------------------------------------------------------------
# ----------------------------------- APP.RUN -------------------------------------
# ---------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()