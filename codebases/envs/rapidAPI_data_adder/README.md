Query from Rapid API 
Backtrader for backtesting.
Auto Historical data fetching.

### ***STARTER GUIDE ***

* it will test RAPID API query to download data from yahoofinance and save it to the desired format under ./data
* change format under line 29 ```return datetime.strptime(timestamp_as_str, "%Y-%m-%d %H:%M:%S")``` at ```auto_data_fetch.py``` if the format is available.
* update line 8,9 for desired currency pair.
* install required packages ```pip install -r requirements.txt```
* running ```python main.py``` will fetch the files for furhter work.