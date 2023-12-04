import time
import sys

import ccxt

import config


exchange = ccxt.ftxus({
    'apikey': config.API_KEY,
    'secret': config.SECRET_KEY
})

ticker = exchange.fetch_ticker(config.SYMBOL)
# print(ticker)

# track orders in the lists
buy_orders = []
sell_orders = []

initial_buy_order = exchange.create_market_buy_order(config.SYMBOL, config.POSITION_SIZE * config.NUM_SELL_GRID_LINES)
# print(initial_buy_order)

for i in range(config.NUM_BUY_GRID_LINES):
    price = ticker['bid'] - (config.GRID_SIZE * (i+1))
    print(f"submitting market limit buy order at price {price}")
    order = exchange.create_limit_buy_order(config.SYMBOL, config.POSITION_SIZE, price)
    buy_orders.append(order)

for i in range(config.NUM_SELL_GRID_LINES):
    price = ticker['bid'] + (config.GRID_SIZE * (i+1))
    print(f"submitting market limit sell order at price {price}")
    order = exchange.create_limit_sell_order(config.SYMBOL, config.POSITION_SIZE, price)
    sell_orders.append(order)

for order in buy_orders:
    print(order)