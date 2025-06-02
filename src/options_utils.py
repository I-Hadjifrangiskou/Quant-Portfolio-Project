import numpy as np
from scipy.stats import norm


# Calculates Black-Scholes price for a European call option
def black_scholes_call_price(S, K, T, r, sigma):

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T)) # Standardised distance between current spot price (S) and strike price (K) with drift term (r + 0.5σ^2) and time of maturity T 
    d2 = d1 - sigma * np.sqrt(T) # Prob. of stock price exceeding strike at expiration

    # Call price
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

# Estimates implied volatility (value of sigma that would make the theoretical price equal to the observed price) using a simple Newton-Raphson algorithm
def implied_volatility_call(C_market, S, K, T, r, tol = 1e-4, max_iter = 200):

    sigma = 0.2  # Initial guess
    
    for i in range(max_iter):

        price = black_scholes_call_price(S, K, T, r, sigma) # Calculate price based on Black-Scholes
        vega = S * norm.pdf((np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))) * np.sqrt(T) # vega = dC/dσ, used for first order expansion. For Black-Scholes, we have a closed form expression.
        diff = price - C_market # Compute difference in price

        # Stop if price difference is below the tolerance value, if not, update sigma and keep iterating
        if abs(diff) < tol:

            return sigma
        
        # σ_(n+1) = σ_n - f(σ_n)/f'(σ_n), where f is the price difference, so f' is just vega. This is the Newton-Raphson update rule
        sigma -= diff / vega
        
    return np.nan  # If it doesn't converge
