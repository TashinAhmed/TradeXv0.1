

def get_macd(price, slow=SMA_SLOW, fast=SMA_FAST, smooth=9):
    price = price.to_frame()
    exp1 = price.ewm(span = fast, adjust = False).mean()
    exp2 = price.ewm(span = slow, adjust = False).mean()
    macd = pd.DataFrame(exp1 - exp2).rename(columns = {'close':'macd'})
    signal = pd.DataFrame(macd.ewm(span = smooth, adjust = False).mean()).rename(columns = {'macd':'signal'})
    hist = pd.DataFrame(macd['macd'] - signal['signal']).rename(columns = {0:'hist'})
    frames =  [macd, signal, hist]
    srs = pd.concat(frames, join = 'inner', axis = 1)
    # print(srs)
    print(srs.macd)
    return macd.squeeze()