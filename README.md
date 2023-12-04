# TradeX v0.1 - [Collections Assembled]
Hub of different automatic trading system including rule based and DeepRL based systems on historical and real time data with Alapaca API

> If you trade a lot, you only need to be right 51 percent of the time, we need a smaller edge on each trade.
> 
> --- Elwyn Berlekamp, co-Founder of Combinatorial Game Theory


The majority of the scripts in this repository automate trading using technical indicators. These scripts cover a range of momentum trading techniques, opening range breakouts, support and resistance reversals, and statistical arbitrage techniques. However, technical analysis is not the only aspect of quantitative trading. It can be used to describe low latency order execution in the market microstructure, pattern recognition on alternative datasets to produce alphas, or computational finance to take advantage of derivative price mismatch. Therefore, this repository contains a few active projects. Most of these projects involve quantitative analysis of odd ideas I come up with to outperform the market (or so I thought). Due to the high cost of acquiring ultra high frequency data, there is no HFT strategy (even consider platforms like Alpaca).

Please take note that most of the scripts are back and forward-tested using historical data, primarily using Python rather than C++. All trades are assumed to be frictionless. No illiquidity, slippage, or surcharge. Last but not least, each script includes a global function called main that enables you to incorporate it directly into your trading platform (too lazy to write appropriate docs and docstrings).

---
***Deep Reinforcement Learninng based Custom Trader (BackTester) Baseline - [DRLCT](https://github.com/TashinAhmed/SANCHO/tree/main/codebases/src/DRLCT)***

> Multiple follow up versions as initial baseline for DeepRL based solutions on multiple trading indicators for historical dataset. Also a custom environment have been created that act as an exchange.

---


***Machine Learning Models on Historical ForEx Dataset - [Forex_Hist_ML_models](https://github.com/TashinAhmed/SANCHO/tree/main/codebases/src/Forex_Hist_ML_models)***
> Implementations were on [Support Vector Regression (SVR)](https://en.wikipedia.org/wiki/Support_vector_machine), [Random Forest](https://en.wikipedia.org/wiki/Random_forest) created and traded with [Oanda API v20](https://developer.oanda.com/).
> modules including:
> - accounts summary
> - historical data handling, normalizations, overall preparation
> - create orders, follow positions, price info in details 

---
***RL and Deep RL based Models on Historical ForEx Dataset - [Forex_Hist_RL_working_agents](https://github.com/TashinAhmed/SANCHO/tree/main/codebases/src/Forex_Hist_RL_working_agents)***
> Implementations of [Q Learning](https://en.wikipedia.org/wiki/Q-learning) based algorithms (trials) with splitted data for train and evaluation.

---
***50 different stocks historical data from Nasdaq - [Nasdaq](https://github.com/TashinAhmed/SANCHO/tree/main/codebases/src/Nasdaq)***
> Created an EDA for analysis, prepared modes with ARIMA, ARIMAxLSTM hybrid and RNN. (notebooks)
> More information: inside the directory.

---
***Oanda API: ForEx trial with RSI technical indicator trial - [OandaAPI_forex](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/OandaAPI_forex)***
> OandaAPI trial with EUR-USD historical data. Trade created with RSi technical indicator.

---
***Proximal Policy Optimization based bot for BTCUSD [RL_BTC_BOT_TRIAL](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/RL_BTC_BOT_TRIAL)***
> Custom multiprocessing environment for hitorical BTCUSD pair. models can be pre loaded before testing and matplotlib GUI for observing BUY-SELL trackers.


---
***Stock Trading Environment: RL/DL based systems (+notebooks) [Stock_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Stock_trading)***
> Multiple shortlisted RL/DL based systems for historical stock trading, more: inside the notebooks [directory](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Stock_trading).

---
***Rule based trading bot [rule_based_hub](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rule_based_hub)***
> alongside multiple trials on rule based bots, more inside the directory. Also a streamlit PoC [showed](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rule_based_hub/streamlit_PoC) for future inference end visualization
> ```streamlit run streamlit.py```

---
***Rule based brokers trial (Alpaca and Binance) for multi-pair environment [rulebased_brokers_trials](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rulebased_brokers_trials)***

---
***Simpler and Scalable Rule based trading bots with logs [tradex_rulebot](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/tradex_rulebot)***
> This can be the directory where anyone can start their findings as this is the work which is much more stable than other experiments. Semi proper logging system is created. all the bots are the refined version of the following one. i.e. bot_#  with the highest (#) value have more potential to beat the market than the previous one. bot 1 - 7 can be ignored because of their improper logs. Rest of the bots are well logged and can be reused with other functions.



## 🖥️ Web Application Trials [webapp_trials](https://github.com/TashinAhmed/TradeX/tree/main/codebases/webapp_trials)
> web apps shows realtime charts and values of quotes and buy and sell only. We were unable to put tickers on the charts. We have used free template from Lightweight charts via tradingview platform (https://jsfiddle.net/TradingView/yozeu6k1/). 
> experiments performed with pure python based frameworks, flask, binance, alpaca API templates.
> Secondary experiments have been performed with JS(TS), vite, tradingview lightweight chart templates.
> TODO: ticker implementations. 


---
---
## [🗑️ Depricated codebases](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated)

- [Alpaca_Polygon_backtrading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Alpaca_Polygon_backtrading)
- [Oanda_telegram_mail_bot_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Oanda_telegram_mail_bot_trial)
- [ftx_grid_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading)
- [ftx_grid_trading_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading_trial)
- [tradingview-webhook-alerts](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/tradingview-webhook-alerts)


## [🛝 custom environments](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs)
- [custom_binance](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/custom_binance)
- [dse_dataloader_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/dse_dataloader_trial)
- [rapidAPI_data_adder](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/rapidAPI_data_adder)

## [ℹ️ source codes](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src)
- [DRLCT](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/DRLCT)
- [Forex_Hist_ML_models](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_ML_models)
- [Forex_Hist_RL_working_agents](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_RL_working_agents)
- [Nasdaq](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Nasdaq)
- [OandaAPI_forex](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/OandaAPI_forex)
- [RL_BTC_BOT_TRIAL](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/RL_BTC_BOT_TRIAL)
- [Stock_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Stock_trading)
- [rule_based_hub](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rule_based_hub)
- [rulebased_brokers_trials](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rulebased_brokers_trials)
- [tradex_rulebot](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/tradex_rulebot)

### Codebases (depreicated) in terms of data type 
| Dir Name | ForEx | Crypto | Stocks |
|-------------| ------------- | ------------- | ------------- |
| [Alpaca_Polygon_backtrading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Alpaca_Polygon_backtrading)    | - | &check; | - |
| [Oanda_telegram_mail_bot_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Oanda_telegram_mail_bot_trial) | &check; | - | - |
| [ftx_grid_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading)              | - | &check; | - |
| [ftx_grid_trading_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading_trial)        | - | &check; | - |
| [tradingview-webhook-alerts](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/tradingview-webhook-alerts)    | - | - | &check; |

### Codebases (depricated) in terms of solution type 
| Dir Name | ML/DL | Deep/RL | Rule based |
|-------------| ------------- | ------------- | ------------- |
| [Alpaca_Polygon_backtrading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Alpaca_Polygon_backtrading)    | - | - | &check; |
| [Oanda_telegram_mail_bot_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Oanda_telegram_mail_bot_trial) | - | - | &check; |
| [ftx_grid_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading)              | - | - | &check; |
| [ftx_grid_trading_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading_trial)        | - | - | &check; |
| [tradingview-webhook-alerts](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/tradingview-webhook-alerts)    | - | - | - |

### Codebases (custom environments) in terms of data type 
| Dir Name | ForEx | Crypto | Stocks |
|-------------| ------------- | ------------- | ------------- |
| [custom_binance](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/custom_binance)    | - | &check; | - |
| [dse_dataloader_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/dse_dataloader_trial) | - | - | &check; |
| [rapidAPI_data_adder](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/rapidAPI_data_adder)              | &check; | - | - |


### Codebases (custom environments) in terms of solution type 
|Dir Name                |AI/DL|RL   |Rule based|
|--------------------|-----|-----|----------|
|[custom_binance](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/custom_binance)      |&check; |&check; |-     |
|[dse_dataloader_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/dse_dataloader_trial)|-|-|&check;      |
|[rapidAPI_data_adder](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/rapidAPI_data_adder) |-|-|&check;      |

### Codebases (source codes) in terms of data type 
|Dir Name                |Forex|Crypto|Stocks|
|--------------------|-----|------|------|
|[DRLCT](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/DRLCT)               |-|&check;  |- |
|[Forex_Hist_ML_models](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_ML_models)|&check; |- |- |
|[Forex_Hist_RL_working_agents](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_RL_working_agents)|&check; |- |- |
|[Nasdaq](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Nasdaq)              |-|- |&check;  |
|[OandaAPI_forex](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/OandaAPI_forex)      |&check; |- |- |
|[RL_BTC_BOT_TRIAL](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/RL_BTC_BOT_TRIAL)    |-|&check;  |- |
|[Stock_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Stock_trading)       |-|- |&check;  |
|[rule_based_hub](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rule_based_hub)      |-|&check;  |- |
|[rulebased_brokers_trials](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rulebased_brokers_trials)|-|&check;  |- |
|[tradex_rulebot](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/tradex_rulebot)      |-|&check;  |- |


### Codebases (source codes) in terms of solution type
|Dir Name            |AI/DL|RL   |Rule based|
|--------------------|-----|-----|----------|
|[DRLCT](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/DRLCT)               |&check; |&check; |-     |
|[Forex_Hist_ML_models](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_ML_models)|&check; |-|-     |
|[Forex_Hist_RL_working_agents](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_RL_working_agents)|&check; |&check; |-     |
|[Nasdaq](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Nasdaq)              |&check; |&check; |-     |
|[OandaAPI_forex](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/OandaAPI_forex)      |-|-|&check;      |
|[RL_BTC_BOT_TRIAL](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/RL_BTC_BOT_TRIAL)    |-|&check; |-     |
|[Stock_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Stock_trading)       |&check; |&check; |-     |
|[rule_based_hub](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rule_based_hub)      |-|-|-     |
|[rulebased_brokers_trials](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rulebased_brokers_trials)|-|-|&check;      |
|[tradex_rulebot](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/tradex_rulebot)      |-|-|&check;      |

### codebases in terms of brokers and exchanges

|Category            |Dir Name|Alpaca|Polygon|Oanda|FTX          |Others       |
|--------------------|--------|------|-------|-----|-------------|-------------|
|depricated          |[Alpaca_Polygon_backtrading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Alpaca_Polygon_backtrading)|&check;  |&check;   |-|-        |-        |
|depricated          |[Oanda_telegram_mail_bot_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Oanda_telegram_mail_bot_trial)|- |-  |&check; |-        |-        |
|depricated          |[ftx_grid_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading)|- |-  |-|&check;         |-        |
|depricated          |[ftx_grid_trading_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading_trial)|- |-  |-|&check;         |-        |
|depricated          |[tradingview-webhook-alerts](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/tradingview-webhook-alerts)|&check;  |-  |-|-        |-        |
|environments (custom)|[custom_binance](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/custom_binance)|- |-  |-|-        |Binance      |
|environments (custom)|[dse_dataloader_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/dse_dataloader_trial)|- |-  |-|-        |-        |
|environments (custom)|[rapidAPI_data_adder](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/rapidAPI_data_adder)|- |-  |-|-        |RapidAPI     |
|source codes        |[DRLCT](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/DRLCT)   |- |-  |-|-        |-        |
|source codes        |[Forex_Hist_ML_models](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_ML_models)|- |-  |&check; |-        |-        |
|source codes        |[Forex_Hist_RL_working_agents](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_RL_working_agents)|- |-  |&check; |-        |-        |
|source codes        |[Nasdaq](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Nasdaq)  |- |-  |-|-        |-        |
|source codes        |[OandaAPI_forex](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/OandaAPI_forex)|- |-  |&check; |-        |-        |
|source codes        |[RL_BTC_BOT_TRIAL](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/RL_BTC_BOT_TRIAL)|- |-  |-|-        |BitFinex     |
|source codes        |[Stock_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Stock_trading)|- |-  |-|-        |-        |
|source codes        |[rule_based_hub](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rule_based_hub)|- |-  |-|-        |RapidsAPI    |
|source codes        |[rulebased_brokers_trials](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rulebased_brokers_trials)|&check;  |-  |-|-        |Binance, ccxt|
|source codes        |[tradex_rulebot](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/tradex_rulebot)|&check;  |-  |-|-        |-        |

### codebases in terms of data availabilty
|Category            |Dir Name|Historical|Realtime|
|--------------------|--------|----------|--------|
|depricated          |[Alpaca_Polygon_backtrading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Alpaca_Polygon_backtrading)|-     |    -    |
|depricated          |[Oanda_telegram_mail_bot_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Oanda_telegram_mail_bot_trial)|&check;      |-   |
|depricated          |[ftx_grid_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading)|-     |&check;    |
|depricated          |[ftx_grid_trading_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading_trial)|-     |&check;    |
|depricated          |[tradingview-webhook-alerts](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/tradingview-webhook-alerts)|-     |&check;    |
|environments (custom)|[custom_binance](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/custom_binance)|&check;      |-   |
|environments (custom)|[dse_dataloader_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/dse_dataloader_trial)|&check;      |-   |
|environments (custom)|[rapidAPI_data_adder](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/rapidAPI_data_adder)|&check;      |-   |
|source codes        |[DRLCT](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/DRLCT)   |&check;      |-   |
|source codes        |[Forex_Hist_ML_models](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_ML_models)|&check;      |-   |
|source codes        |[Forex_Hist_RL_working_agents](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_RL_working_agents)|&check;      |-   |
|source codes        |[Nasdaq](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Nasdaq)  |&check;      |-   |
|source codes        |[OandaAPI_forex](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/OandaAPI_forex)|&check;      |-   |
|source codes        |[RL_BTC_BOT_TRIAL](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/RL_BTC_BOT_TRIAL)|&check;      |-   |
|source codes        |[Stock_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Stock_trading)|&check;      |-   |
|source codes        |[rule_based_hub](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rule_based_hub)|&check;      |-   |
|source codes        |[rulebased_brokers_trials](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rulebased_brokers_trials)|-     |&check;    |
|source codes        |[tradex_rulebot](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/tradex_rulebot)|-     |&check;    |


### codebases that have visualizer/logs and scalibilty opportunities
|Category            |Dir Name|Plot/Log|Scalable|
|--------------------|--------|--------|--------|
|depricated          |[Alpaca_Polygon_backtrading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Alpaca_Polygon_backtrading)|No      |yes (40%)|
|depricated          |[Oanda_telegram_mail_bot_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/Oanda_telegram_mail_bot_trial)|No      |No      |
|depricated          |[ftx_grid_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading)|No      |No      |
|depricated          |[ftx_grid_trading_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/ftx_grid_trading_trial)|No      |No      |
|depricated          |[tradingview-webhook-alerts](https://github.com/TashinAhmed/TradeX/tree/main/codebases/depricated/tradingview-webhook-alerts)|No      |No      |
|environments (custom)|[custom_binance](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/custom_binance)|No      |No - have custom environment|
|environments (custom)|[dse_dataloader_trial](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/dse_dataloader_trial)|Yes     |No - exception, worked on DSE|
|environments (custom)|[rapidAPI_data_adder](https://github.com/TashinAhmed/TradeX/tree/main/codebases/envs/rapidAPI_data_adder)|No      |No      |
|source codes        |[DRLCT](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/DRLCT)   |yes     |Yes - custom env|
|source codes        |[Forex_Hist_ML_models](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_ML_models)|Yes     |No      |
|source codes        |[Forex_Hist_RL_working_agents](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Forex_Hist_RL_working_agents)|Yes     |No - notebooks|
|source codes        |[Nasdaq](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Nasdaq)  |Yes     |No - notebooks|
|source codes        |[OandaAPI_forex](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/OandaAPI_forex)|No      |No      |
|source codes        |[RL_BTC_BOT_TRIAL](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/RL_BTC_BOT_TRIAL)|Yes     |Yes - custom env|
|source codes        |[Stock_trading](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/Stock_trading)|Yes     |Yes - custom env + notebooks|
|source codes        |[rule_based_hub](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rule_based_hub)|Yes     |Streamlit PoC|
|source codes        |[rulebased_brokers_trials](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/rulebased_brokers_trials)|Yes     |No      |
|source codes        |[tradex_rulebot](https://github.com/TashinAhmed/TradeX/tree/main/codebases/src/tradex_rulebot)|Yes     |Yes     |


## Utilized Methods more or less
- [AI Methods](https://github.com/TashinAhmed/TradeX/tree/main/codebases/methods/AI_methods)
- [Technical Indicators](https://github.com/TashinAhmed/TradeX/tree/main/codebases/methods/technical_indicators)