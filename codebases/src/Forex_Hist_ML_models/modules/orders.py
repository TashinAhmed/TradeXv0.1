
import json
from connection import Connection
import oandapyV20.endpoints.orders as orders

def createOrder(units, instrument):
    # Load config
    connection = Connection()
    accountID = connection.config['ACCOUNT_ID']
    
    # Load json
    with open('orderbody.json', 'r') as f:
        data = json.load(f)
        
    # set units and instrument
    data['order']['units'] = units
    data['order']['instrument'] = instrument
    print('Create Order Request: {}\n'.format(data))
    
    # Request
    r = orders.OrderCreate(accountID, data)
    return connection.API.request(r)
