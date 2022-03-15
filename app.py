from flask import Flask, jsonify
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
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slqite.db' #three /// make path relative
# db = SQLAlchemy(app)

# ---------------------------------------------------------------------------------
# ----------------------------------- MODELS --------------------------------------
# ---------------------------------------------------------------------------------

# Import models for flask sql alchemy

# ---------------------------------------------------------------------------------
# ----------------------------------- ROUTES --------------------------------------
# ---------------------------------------------------------------------------------

#example route
@app.route('/ping', methods=['GET'])
def ping_pong():
    a= [
        {"Ticker":'APPL', "Price":143},
        {"Ticker":'MSFT', "Price":220}
    ]
    return jsonify(a)

# get current portofolio data, ticker, current price, market value, etc...
@app.route('/getPortofolio', methods=['GET'])
def getPortofolio():

    portofolio=getInvestingData() #function imported from portofolio.py file

    return jsonify(portofolio)

@app.route('/historicDividends',methods=['GET'])
def getHisotoricDividends():

    historicDividends=getPortofolioDividends() #funciton imported from portofolioDivindeds.py

    return jsonify(historicDividends)

if __name__ == '__main__':
    app.run()