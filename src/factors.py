import pandas as pd

# Calculates momentum - percentage change over a lookback window characterised by n trading days
def calculate_momentum(prices, n = 126):

    return prices.pct_change(n)


# Calculates volatility (measure of stock price fluctuation) - polling standard deviation of daily returns for a number of days given by window; gives a risk estimate 
def calculate_volatility(prices, window = 63):
    
    return prices.pct_change().rolling(window).std()


# Calculates a simple moving average crossover signal (not used right now)
def calculate_sma_signal(prices, short = 20, long = 100):

    return (prices.rolling(short).mean() > prices.rolling(long).mean()).astype(int)


# Calculates z-score normalized factors
def calculate_zscore(df):

    return (df - df.mean(axis = 1, skipna = True).values[:, None]) / df.std(axis = 1, skipna = True).values[:, None]
