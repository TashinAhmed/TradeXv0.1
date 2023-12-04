custom environment trial with binance on a dummy action that can be used as rule nbased learning or any other AI based systems. a plot visualizer also been added that have been tested for different historical dataset. Run `binanceEnv.py` to test the env.

historical data for crypto.


## ***STARTER GUIDE***

* works with historical data only
* put the data in /data directory in csv/xls format.
* if you want to import data from binance you can just run ```python Binance_to_excel.py```
* before that change line 7,8 and update the credentials.
* put currency pair under line 66, at default it is given 'BTCUSDT'.
* ```pyhton bot.py``` will trigger the cutom crypto trading env written under ```binanceEnv.py``` via a webhook.
* a visualizer will generate alongside through ```Visualization.py``` that will plot buy and sell on the line graph.