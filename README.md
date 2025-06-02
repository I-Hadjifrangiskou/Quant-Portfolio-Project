# Factor-Based Portfolio Construction and Evaluation

This project explores the development and evaluation of systematic equity portfolios using traditional quant factors and machine learning techniques. Inspired by techniques used in industry, the goal is to build a replicable backtesting pipeline that connects signal generation, risk modeling, and portfolio optimization.

## Objectives
- Construct financial factors (momentum, volatility, value, etc.)
- Build and backtest systematic equity portfolios
- Use ML models to enhance signal generation
- Evaluate performance using industry-standard metrics

## Project Structure
- `notebooks/`: Exploratory analysis and results
- `src/`: Core project modules (factors, optimizers, backtest engine)
- `data/`: Cached data from Yahoo Finance or other APIs
- `reports/`: Visualizations and evaluation outputs

## Technologies Used
- Python (Pandas, NumPy, scikit-learn, yfinance, matplotlib, seaborn)
- ML Models: Linear regression, random forest, XGBoost
- Optimization: cvxpy, scipy

## Next Steps
- Add alternative data sources
- Experiment with deep learning-based factor modeling
- Deploy interactive dashboard (e.g. Streamlit)
