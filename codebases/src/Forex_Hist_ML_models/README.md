Implementations were on [Support Vector Regression (SVR)](https://en.wikipedia.org/wiki/Support_vector_machine), [Random Forest](https://en.wikipedia.org/wiki/Random_forest) created and traded with [Oanda API v20](https://developer.oanda.com/).
 modules including:
 - accounts summary
 - historical data handling, normalizations, overall preparation
 - create orders, follow positions, price info in details 


order body
```
{
  "order": {
    "units": "",
    "instrument": "",      
    "timeInForce": "FOK",
    "type": "MARKET",
    "positionFill": "DEFAULT"
  }
}
```

```helper``` - it will parse candle diagram according to desired format, at default - daily basis.

```models``` - SVR and RandomForest (can be altered with any sklearn regression models)

```modules``` - 
* account summary - will provide a/c summary in terms of a/c IDs, 
* historical data processing for backtesting - will request Oanda API for data , 
* orders creation - create orders (todo), 
* position tracking - check current position status, 
* price related informations - current market status, bid price, asking price, tradeable quantity and so on.

run ```python tradingbot.py```