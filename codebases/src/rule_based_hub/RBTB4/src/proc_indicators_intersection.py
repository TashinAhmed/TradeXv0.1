
def indicatorsIntersection(df):
    ema_20_100_diff = df["ema20"] - df["ema100"]
    ema_100_200_diff = df["ema100"] - df["ema200"]
    ema_20_200_diff = df["ema20"] - df["ema200"]
    ema100_BBH_diff = df["ema100"] - df["BBH"]
    ema200_BBH_diff = df["ema200"] - df["BBH"]
    ema100_BBL_diff = df["ema100"] - df["BBL"]
    ema200_BBL_diff = df["ema200"] - df["BBL"]

    df["ema_20_100_diff"] = ema_20_100_diff
    df["ema_100_200_diff"] = ema_100_200_diff
    df["ema_20_200_diff"] = ema_20_200_diff
    df["ema100_BBH_diff"] = ema100_BBH_diff
    df["ema200_BBH_diff"] = ema200_BBH_diff
    df["ema100_BBL_diff"] = ema100_BBL_diff
    df["ema200_BBL_diff"] = ema200_BBL_diff