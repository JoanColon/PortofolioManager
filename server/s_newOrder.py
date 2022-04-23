from s_getExchangeRates import getExchangeRates

def getNewOrderCurrencyRate(currency):
    CurrencyRate_dict=getExchangeRates()

    currencyRate=CurrencyRate_dict[currency]

    return currencyRate
