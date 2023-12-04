
from connection import Connection
import oandapyV20.endpoints.positions as positions

def getOpenPosition():
    # Load config
    connection = Connection()
    accountID = connection.config['ACCOUNT_ID']

    # Request
    r = positions.OpenPositions(accountID)
    return connection.API.request(r)

