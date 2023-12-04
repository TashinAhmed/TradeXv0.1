import backtrader
import datetime
import auto_data_fetch

initial_amount = int(input("input your initial amount: "))
trade_count = int(input("How many trades you want to buy/sell at single timestamp: "))

cerebro = backtrader.Cerebro()
cerebro.broker.set_cash(initial_amount)

data = backtrader.feeds.YahooFinanceCSVData(
    dataname = auto_data_fetch.csv_filename,
    fromdate = datetime.datetime(2000, 1, 1),
    todate = datetime.datetime(2000, 12, 31),
    reverse = False,
)

cerebro.adddata(data)