
from connection import Connection
import oandapyV20.endpoints.instruments as instruments

def getData(instrument, day, granularity):    
    # Request
    connection = Connection()
    params = {"count": day, "granularity": granularity}
    r = instruments.InstrumentsCandles(instrument, params)
    return connection.API.request(r)




