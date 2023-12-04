a collection of notebooks for deep learning based forecasting models and (deep) reinforcement learning based decision making bots in the ```notebooks``` directory.

```rl_agents``` directory have a simpler file like structure for the above scenario.  
run ```python main.py``` to observe a RL based model.

![Outcomes](codebases/src/Stock_trading/assets/RL-DRL-outcomes.png")

* Also a classic PPO generated bot under /rl_agents
* run `python main.py`
* tweak this params 
```MAX_ACCOUNT_BALANCE = 2147483647
    MAX_NUM_SHARES = 2147483647
    MAX_SHARE_PRICE = 5000
    MAX_OPEN_POSITIONS = 5
    MAX_STEPS = 20000
    INITIAL_ACCOUNT_BALANCE = 10000```

under `StockTradingEnv.py`

