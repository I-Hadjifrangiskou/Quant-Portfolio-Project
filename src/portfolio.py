
# Select the top n% stocks per date, based on the factor rank (here factor_df will usually be the momentum)
def top_n_percent_signal(factor_df, pct = 0.2):

    ranks     = factor_df.rank(axis = 1, ascending = False) # Rank stocks across each date
    threshold = int(factor_df.shape[1] * pct) # Cutoff rank, i.e. get the top pct ranks 
    signal    = (ranks <= threshold).astype(int) # Set the signal of ranks above the threshold to 1, rest to 0

    return signal

# Simple function which gives equal weight to the selected stocks
def build_portfolio(returns, signal):
    
    weights = signal.div(signal.sum(axis=1), axis = 0).fillna(0) # Weights of selected stocks, this applies equal weights to all stocks, i.e. converts the 1s from the signal into 1/N where N is the number of stocks that passed the threshold
    portfolio_returns = (weights.shift(1) * returns).sum(axis = 1) # Sums the result of the daily returns to get overall portfolio result

    return portfolio_returns
