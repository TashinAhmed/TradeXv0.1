
from connection import Connection
import oandapyV20.endpoints.pricing as pricing


def getCurrentPrice(instrument):
    # Load config
    connection = Connection()
    accountID = connection.config['ACCOUNT_ID']
    
    # Request
    params = {"instruments": instrument}
    r = pricing.PricingInfo(accountID, params)
    return connection.API.request(r)

def parsePriceInfo(price_info):
    currencies = {}

    for currency in price_info['prices']:
        # Extract the currency information
        instrument = currency['instrument']
        tradeable = currency['tradeable']
        bid = currency['closeoutBid']
        ask = currency['closeoutAsk']
        print('{} currently {}.'.format(instrument, 'available' if tradeable else 'not available'))
        print('Bid: {}, Ask: {}\n'.format(bid, ask))
        
        # Convert to desired structure
        currencies[instrument] = {}
        currencies[instrument]['tradeable'] = tradeable
        currencies[instrument]['bid'] = float(bid)
        currencies[instrument]['ask'] = float(ask)

    return currencies
        
        
