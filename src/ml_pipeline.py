
# Combines dataframes of multiple factors, aligns them with forward returns of lookahead days
def ml_dataset(factor_dfs, returns, lookahead = 1):

    import pandas as pd

    # Stack each factor into long format
    stacked_factors = []
    for name, df in factor_dfs.items():
        stacked = df.stack()
        stacked.name = name
        stacked_factors.append(stacked)

    # Combine into a single long DataFrame
    features = pd.concat(stacked_factors, axis=1)

    # Target: forward return
    y = returns.shift(-lookahead).stack()
    y.name = 'return'

    # Align features and target
    common_index = features.index.intersection(y.index)
    features = features.loc[common_index]
    y = y.loc[common_index]

    # Combine
    df = features.copy()
    df['return'] = y

    return df.dropna() # Remove NANs

# Trains a model (model_cls) to predict returns from the features. Returns predicted scores 
def train_and_predict_model(df, model_cls, test_fraction = 0.2):
    
    import pandas as pd
    from sklearn.base import clone

    # List of dates, create cutoff of list using the fraction of data to be trained/tested, test_fraction gives the latter
    all_dates = sorted(df.index.get_level_values(0).unique())
    cutoff = int(len(all_dates) * (1 - test_fraction))
    train_dates = all_dates[:cutoff]
    test_dates = all_dates[cutoff:]

    # Training and testing dataframes
    train_df = df[df.index.get_level_values(0).isin(train_dates)]
    test_df = df[df.index.get_level_values(0).isin(test_dates)]

    # ML model chosen as argument model_cls
    model = clone(model_cls)
    model.fit(train_df.drop(columns = 'return'), train_df['return'])

    # Predict using trained model
    test_df = test_df.copy()
    test_df['predicted_return'] = model.predict(test_df.drop(columns='return'))

    return test_df['predicted_return'].unstack()
