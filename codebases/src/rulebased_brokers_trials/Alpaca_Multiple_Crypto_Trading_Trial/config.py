from alpaca_trade_api.rest import REST, TimeFrame

API_KEY = ''
SECRET_KEY = ''

# API_KEY = "<Your API here>"
# SECRET_KEY = "<Your secret key here>"

#---------------- API INFO ----------------#
api = REST(API_KEY,
                    SECRET_KEY,
                    'https://paper-api.alpaca.markets')

#-------- Here basket of stocks ------------#
# symbols = ['AA', 'AAL', 'UAL', 'NIO', 'AMD', 'TSLA', 'BYND', 'NKLA', 'XPEV', 'NVDA']
symbols = ['ETHUSD']


#---- NUMBER OF SHARES FOR EACH PURCHASE -----#
# loading = {'AA': 50,
#            'AAL': 50,
#            'UAL': 50,
#            'NIO': 50,
#            'AMD': 50,
#            'TSLA': 10,
#            'BYND': 20,
#            'NKLA': 30,
#            'XPEV': 30,
#            'NVDA': 50}

loading = {'ETHUSD': 3}

#---- SET SLOW AND FAST MOVING AVERAGE -----#
slow = 12
fast = 34

#------- FREQUENCY for you time interval -----------#
freq = '1Min'