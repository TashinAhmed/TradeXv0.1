from alpaca_trade_api.rest import REST, TimeFrame

API_KEY = 'PKJNXIU9HQQMKYR0KBD6'
SECRET_KEY = 'kALQ9U7GdQ1oU7XUlCYXesVVUNyVUjvtFHgeDGjr'

# API_KEY = "<Your API here>"
# SECRET_KEY = "<Your secret key here>"

#---------------- API INFO ----------------#
api = REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets')

# Check if the market is open now.
clock = api.get_clock()
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

# Check when the market was open on Dec. 1, 2018
date = '2022-09-20'
calendar = api.get_calendar(start=date, end=date)[0]
print('The market opened at {} and closed at {} on {}.'.format(
    calendar.open,
    calendar.close,
    date
))