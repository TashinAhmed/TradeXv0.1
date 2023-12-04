## *** STARTER GUIDE***
run ```python bot_#.py``` to test each and every scale of rule based codes.
They are simple HFT or MFT algorithms on real time data from Alpaca API.
Switch API key and secret keys from the codebases of your own.

files that needs attention,
- ```bot_8_ichimoku.py```

created ichimoku kino hyo based indicator and implemented simple logic that can be scaled up towards multiple logic for actions. 


- ```bot_9_simple_HFT.py```

Faster trading algorithm and tuned to trade faster than other modules.


* provide Alpaca credentials in each file before run them.


* update params in each file for initial positions.
```SYMBOL = 'ETHUSD'
    SMA_FAST = 12
    SMA_SLOW = 24
    QTY_PER_TRADE = 1
    QTY_PER_SELL = 0
    MAX_CLOSE_PRICE = 0.0000000000001
    INIT_BALANCE = 100000000
    BAR_TIME = 0```

* conditional (if-else based) arrangements provided for every settings.
