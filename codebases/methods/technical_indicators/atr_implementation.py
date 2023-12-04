def ma(Data, lookback, what, where):
    for i in range(len(Data)):
        try:
            Data[i, where] = (Data[i - lookback + 1:i + 1, what].mean())
        except IndexError:
            pass
    return Data
def ema(Data, alpha, lookback, what, where):
    """
    - alpha is the smoothing factor
    - window is the lookback period
    - what is the column that needs to have its average calculated
    - where is where to put the exponential moving average
    """
    alpha = alpha / (lookback + 1.0)
    beta  = 1 - alpha
    # First value is a simple SMA
    Data = ma(Data, lookback, what, where)
    # Calculating first EMA
    Data[lookback + 1, where] = (Data[lookback + 1, what] * alpha) + (Data[lookback, where] * beta)
    # Calculating the rest of EMA
    for i in range(lookback + 2, len(Data)):
            try:
                Data[i, where] = (Data[i, what] * alpha) + (Data[i - 1, where] * beta)
            except IndexError:
                pass
    return Data

# The function to add a certain number of columns
def adder(Data, times):
    for i in range(1, times + 1):
        z = np.zeros((len(Data), 1), dtype = float)
        Data = np.append(Data, z, axis = 1)                   
    return Data


# The function to deleter a certain number of columns
def deleter(Data, index, times):
    for i in range(1, times + 1):
        Data = np.delete(Data, index, axis = 1)               
    return Data

# The function to delete a certain number of rows from the beginning
def jump(Data, jump):
    Data = Data[jump:, ]
    return Data




def ATR(Data, lookback, high, low, close, where):
    # From exponential to smoothed moving average   
    lookback = (lookback * 2) - 1
    # True Range
    for i in range(len(Data)):
        try:
            Data[i, where] = max(Data[i, high] - Data[i, low],
                       abs(Data[i, high] - Data[i - 1, close]),
                       abs(Data[i, low] - Data[i - 1, close]))
            
        except ValueError:
            pass
        
    Data[0, where] = 0    
    Data = ema(Data, 2, lookback, where, where + 1)
    Data = deleter(Data, where, 1)
    Data = jump(Data, lookback)
    return Data