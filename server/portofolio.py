import os
import pandas as pd

def getInvestingData():
    cwd=os.getcwd()
    path=os.path.join(cwd,'server','data','FreedomFund_Holdings.csv')

    df=pd.read_csv(path)
    FreedomFund=df.loc[:,['Name','Symbol','Amount','CurrentPrice','MarketValue','Weight']]
    FreedomFund=FreedomFund.to_dict(orient='records')
    
    return FreedomFund
