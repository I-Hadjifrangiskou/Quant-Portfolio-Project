# Quant Portfolio Strategy Exploration

This project explores a series of quantitative strategies for equity portfolio construction, based on both hand-crafted factor signals and machine learning predictions. It is structured to simulate how a quant research team would approach building, evaluating, and comparing different alpha models using real financial data.

---

## Repository Structure

```
factor_portfolio_project/
├── src/
│   ├── factors.py              # Factor computations: momentum, z-score
│   ├── volatility_factors.py   # Volatility metrics and VRP calculation
│   ├── portfolio.py            # Signal creation and portfolio returns
│   ├── ml_pipeline.py          # ML model training and prediction logic
├── data/processed/             # CSV files for prices, returns, factor data
├── notebooks/
│   ├── factor_analysis.ipynb
│   ├── backtest_and_signal.ipynb
│   ├── comparison.ipynb
│   ├── ml_alpha_model.ipynb
```

---

## 1. Factor-Based Portfolios

We constructed and backtested portfolios using several well-known quant factors:

### Momentum

- Calculated using a 6-month return (126-day lookback).
- Ranked cross-sectionally and top 20% selected daily.

### Volatility Risk Premium (VRP)

- Defined as the difference between implied volatility and realized volatility.
- Implied volatility was calculated using the Black-Scholes formula by inverting observed option prices for a single day (ATM call options).
- We assumed this implied volatility to be fixed over the entire date range for each stock, a simplification that reduces noise but does not reflect real market dynamics.
- Realized volatility was computed as the rolling 21-day standard deviation of returns, annualized.

### Combined Factor

- A z-score normalized combination of momentum and VRP.
- Equal-weighted composite score used to rank stocks and select top 20% for portfolio construction.

### Results

- All three factor strategies were evaluated using cumulative returns, Sharpe ratios, and drawdowns.
- The combination of momentum and VRP outperformed the individual strategies in this dataset, showing the value of multi-factor integration.

#### Strategy Performance Plots

**Momentum Strategy vs. Benchmark**  
![Momentum Strategy](../data/processed/momentum-strategy.png)

[Momentum Strategy <src="../data/processed/momentum-strategy.png">](https://github.com/I-Hadjifrangiskou/Quant-Portfolio-Project/blob/main/data/processed/momentum-strategy.png))

**VRP Strategy vs. Benchmark**  
![VRP Strategy](../data/processed/VRP-strategy.png)

**Combined Momentum + VRP Strategy vs. Benchmark**  
![Combined Strategy](../data/processed/Combined-strategy.png)

---

## 2. Machine Learning Strategy

We implemented a machine learning model to predict future returns from factor inputs:

- **Inputs (Features):**
  - Z-score normalized momentum and VRP.

- **Target:**
  - Next-day return (also tested with 5-day lookahead).

- **Model:**
  - Ridge Regression (regularized linear model), selected for its robustness in low-sample settings.
  - Training was done on the first 80% of the date range, and predictions were made for the remaining 20%.

- **Portfolio Construction:**
  - Stocks were ranked daily by predicted return.
  - Top 20% selected to build an equal-weighted portfolio.

### Results

- The ML strategy underperformed compared to simple factor-based strategies.
- Example: ML strategy reached a growth factor of ~1.3 over the test period, while the combined factor strategy reached ~3.5.

#### ML Strategy Plot

![ML Strategy](../data/processed/ML-strategy.png)

### Potential Reasons for Underperformance

- Low number of stocks (only 5 tickers), limiting cross-sectional learning.
- Daily returns are noisy and hard to predict.
- Possible overfitting or insufficient signal strength in the features.
- The top-n portfolio construction method may discard useful predictive signals when the model output is tightly clustered.

---

## Key Takeaways

- Simple, well-engineered factor models (momentum, VRP) can outperform ML-based strategies in low-data regimes.
- Machine learning requires careful tuning, validation, and large, diverse datasets to show its full power in return prediction.
- Model comparison, performance attribution, and robustness testing are essential parts of quant strategy evaluation.

---

## Future Improvements

- Use rolling-window ML training for a more realistic backtest.
- Try additional features (e.g., price volatility, beta, sector dummies).
- Expand the stock universe to improve cross-sectional depth.
- Apply transaction cost simulation and turnover-based penalties.
- Experiment with score-weighted rather than binary top-N portfolios.

---

## Author

Ioannis Hadjifrangiskou  
This project is part of a self-directed effort to explore quantitative research methods and prepare for roles in systematic investing or quant finance.
