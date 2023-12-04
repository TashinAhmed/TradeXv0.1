import json
import requests
import pprint

import config




BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = BASE_URL + "/v2/account"
ORDERS_URL = BASE_URL + "/v2/orders"
HEADERS = {'APCA-API-KEY-ID': config.API_KEY, "APCA-API-SECRET-KEY": config.SECRET_KEY}

def get_account():
    req = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(req.content)


# reference: https://alpaca.markets/docs/api-references/trading-api/orders/#order-entity
def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force # gtc = googd till cancelled
    }
    req = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(req.content)


def get_orders():
    req = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(req.content)

# pprint.pprint(get_account())

# CREATE ORDERS
# response = create_order("ETHUSD", 1, "buy", "market", "gtc")
response = create_order("BTCUSD", 1, "sell", "market", "gtc")
pprint.pprint(f"-> response: {response}")


# GET ORDERS
orders = get_orders()
pprint.pprint(f"-> orders: {orders}")