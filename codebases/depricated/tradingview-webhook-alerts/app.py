from chalice import Chalice
import requests
import json

app = Chalice(app_name='tradingview-webhook-alerts')

# ALPACA bases
API_KEY = "PK509UGLQNV0IRZIRCJ3"
SECRET_KEY = "1dj9k5gE9uddtP6DTYZ7T0852G8zrAJxkyZOnNmG"
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = BASE_URL + "/v2/account"
ORDERS_URL = BASE_URL + "/v2/orders"
HEADERS = {'APCA-API-KEY-ID': API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}


@app.route('/')
def index():
    return {'hello': 'stocks'}

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    request = app.current_request
    webhook_message = request.json_body

    data = {
        "symbol": webhook_message['ticker'],
        "qty": 1,
        "side": "buy",
        "type": "market",
        "time_in_force": "gtc"
    }


    req = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    response = json.loads(req.content)
    print(response)
    print(response.keys())
    return {
        'message': 'Bought stocks !!!',
        'webhook_message': webhook_message
    }
