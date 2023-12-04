

from connection import Connection
import oandapyV20.endpoints.accounts as accounts

def getSummary():    
    # Request
    connection = Connection()
    accountID = connection.config['ACCOUNT_ID']
    r = accounts.AccountSummary(accountID)
    return connection.API.request(r)