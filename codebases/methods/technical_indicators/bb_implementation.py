# Returns a series with the moving average
def get_sma(series, periods):
    return series.rolling(periods).mean()

# Returns a series with the BB Up and Down
def get_bollinger_bands(prices, rate=20):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()
    bollinger_up = sma + std * 2 # Calculate top band
    bollinger_down = sma - std * 2 # Calculate bottom band
    return bollinger_up, bollinger_down