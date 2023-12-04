# DRLCT

Deep Reinforcement Learninng based Custom Trader (BackTester)
> A custom environment for trading with historical data with DeepRL algorithms


## ***STARTER GUIDE ***
Requirements: 

- certifi==2021.10.8
- cycler==0.11.0
- fonttools==4.28.2
- kiwisolver==1.3.2
- matplotlib==3.5.0
- mplfinance==0.12.7a17
- numpy==1.21.4
- opencv-python==4.5.4.60
- packaging==21.3
- pandas==1.3.4
- Pillow==8.4.0
- pyparsing==3.0.6
- python-dateutil==2.8.2
- pytz==2021.3
- setuptools-scm==6.3.2
- six==1.16.0
- tomli==1.2.2
- wincertstore==0.2

in each version there is file called ```trading_bot.py```

Run ```python trading_bot.py```


## v0.1
> Initial random walk on trading and pre solid environment as an exchange.

## v0.2
> Multiple tests on Actor-Critic agent, an overlay of v0.1. CNN and LSTM model have been used as shared models.

`2021-11-13 18:45, 1277.39_Crypto_trader, test episodes:1000, net worth:1054.483903083776, orders per episode:140.566, no profit episodes:14, comment: Dense network`

`2021-11-13 20:45, 1772.66_Crypto_trader, test episodes:1000, net worth:1008.5786807732876, orders per episode:134.177, no profit episodes:341, comment: CNN network`

`2021-11-13 21:15, 1124.03_Crypto_trader, test episodes:1000, net worth:1034.3430652376387, orders per episode:70.152, no profit episodes:55, comment: CNN network`

`2021-11-13 21:31, 1076.27_Crypto_trader, test episodes:1000, net worth:1027.3897665208062, orders per episode:323.233, no profit episodes:303, comment: LSTM network`


## v0.3
> Applied bots based on indicators value like RSI, MACD, PSAR, BB and SMA
- [Moving average convergence/divergence](https://www.investopedia.com/terms/m/macd.asp)
- [Relative Strength Index](https://www.investopedia.com/terms/r/rsi.asp)
- [Parabolic Stop and Reverse](https://www.investopedia.com/terms/p/parabolicindicator.asp)
- [Bollinger Band](https://www.investopedia.com/terms/b/bollingerbands.asp)
- [Simple Moving Average](https://www.investopedia.com/terms/s/sma.asp)



run ```python v0.3/trading_bot.py```

It will trigger a custom agent for backtesting, save logs, a custom environment that can hold balance, provide rewards, also rewards punish value differently. Action can be taken by comparing multiple technical indicators that are scalable to multiple and can be added on line numbers (233)

```self.indicators_history.append([self.df.loc[self.current_step, 'sma7'] / self.normalize_value,
      self.df.loc[self.current_step, 'sma25'] / self.normalize_value,
      self.df.loc[self.current_step, 'sma99'] / self.normalize_value,
      self.df.loc[self.current_step, 'bb_bbm'] / self.normalize_value,
      self.df.loc[self.current_step, 'bb_bbh'] / self.normalize_value,
      self.df.loc[self.current_step, 'bb_bbl'] / self.normalize_value,
      self.df.loc[self.current_step, 'psar'] / self.normalize_value,
      self.df.loc[self.current_step, 'MACD'] / 400,
      self.df.loc[self.current_step, 'RSI'] / 100
])```

This agent system will test 50 times atleast to find the best placement for the agent.                                 
