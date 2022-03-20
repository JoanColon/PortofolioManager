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
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slqite.db' #three /// make path relative
# db = SQLAlchemy(app)

# ---------------------------------------------------------------------------------
# ----------------------------------- MODELS --------------------------------------
# ---------------------------------------------------------------------------------

# Import models for flask sql alchemy

# ---------------------------------------------------------------------------------
# ----------------------------------- ROUTES --------------------------------------
# ---------------------------------------------------------------------------------

# get current portofolio data, ticker, current price, market value, etc. SEND TO "ViewPortofolio.vue"
@app.route('/getPortofolio', methods=['GET'])
def getPortofolio():

    portofolio=getInvestingData() #function imported from portofolio.py file

    return jsonify(portofolio)

# get historic dividend data. SEND TO "ViewDividends.vue"
@app.route('/historicDividends',methods=['GET'])
def getHisotoricDividends():

    historicDividends=getPortofolioDividends() #funciton imported from portofolioDivindeds.py

    return jsonify(historicDividends)

#get data when entering a new order. GET DATA FROM "ViewPortofolio.vue"
@app.route('/postNewOrder', methods=['GET','POST'])
def getVueData():

    postData=request.get_json(force=True)
    print(postData)
    
    return jsonify('data uploaded to database')


if __name__ == '__main__':
    app.run()