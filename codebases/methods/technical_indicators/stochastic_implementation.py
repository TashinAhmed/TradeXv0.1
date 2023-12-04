import numpy as np


# The function to add a certain number of columns
def adder(Data, times):
    for i in range(1, times + 1):
        z = np.zeros((len(Data), 1), dtype=float)
        Data = np.append(Data, z, axis=1)
    return Data

# The function to deleter a certain number of columns


def deleter(Data, index, times):
    for i in range(1, times + 1):
        Data = np.delete(Data, index, axis=1)
    return Data

# The function to delete a certain number of rows from the beginning


def jump(Data, jump):
    Data = Data[jump:, ]
    return Data


def stochastic(Data, lookback, high, low, close, where):
    Data = adder(Data, 1)

    for i in range(len(Data)):
        try:
            Data[i, where] = (Data[i, close] - min(Data[i - lookback + 1:i + 1, low])) / (
                max(Data[i - lookback + 1:i + 1, high]) - min(Data[i - lookback + 1:i + 1, low]))
        except ValueError:
            pass

        Data[:, where] = Data[:, where] * 100
        Data = jump(Data, lookback)
    return Data
