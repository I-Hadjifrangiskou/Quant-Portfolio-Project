import pandas as pd

# Compute realized volatility, taken to be the rolling standard deviation of daily returns for ndays trading days.
def calculate_realized_volatility(returns, ndays):

    return returns.rolling(ndays).std()

# Compute the difference between the implied volatility calculated through Black-Scholes and the realized volatility for each stock over time (volatility risk premium)
def iv_realized_diff(iv_series, realized_vol_series):

    # A positive value may imply overpricing, whereas a negative value may be underestimating future volatility (depending how reliable the underlying mathematical model is)
    return iv_series - realized_vol_series
