"""
NASDAQ-100 index - Machine Learning-Driven Algo Quantitative Trading Strategy
                    with Systematic Market Prediction Framework

@author: Kristijan <kristijan.sarin@gmail.com>
"""

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# 1. Load data
def load_data(ticker="^NDX", period="max", interval="1d"):
    return yf.download(ticker, period=period, interval=interval)

# Load macro data
def load_macroeconomic_data():
    tickers = {'US10Y': '^TNX', 'DXY': 'DX-Y.NYB', 'WTI': 'CL=F', 'Gold': 'GC=F', 'VIX': '^VIX'}
    data = {}
    for name, ticker in tickers.items():
        data[name] = yf.download(ticker, period='max', interval='1d')['Close']
    return pd.DataFrame(data)

# 2. Add indicators
def add_technical_indicators(df, macro_df):
    # RSI
    df['RSI_14'] = df['Close'].rolling(window=14).apply(lambda x: np.mean(x[x > np.mean(x)]) / np.mean(x))

    # MA
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()

    # BB
    df['20_day_MA'] = df['Close'].rolling(window=20).mean()
    df['20_day_STD'] = df['Close'].rolling(window=20).std()
    df['Upper_Band'] = df['20_day_MA'] + (df['20_day_STD'] * 2)
    df['Lower_Band'] = df['20_day_MA'] - (df['20_day_STD'] * 2)

    # On-Balance Volume
    df['OBV'] = (np.sign(df['Close'].diff()) * df['Volume']).fillna(0).cumsum()

    # Momentum Indicator: Rate of Change
    df['Momentum'] = df['Close'].diff(1)

    # Lagged Features (Previous 1, 2, and 3 periods)
    df['Lag_1'] = df['Close'].shift(1)
    df['Lag_2'] = df['Close'].shift(2)
    df['Lag_3'] = df['Close'].shift(3)

    # Cross-correlating US100 stocks and macro data
    df = df.join(macro_df, how='inner').fillna(method='ffill')

    # Add future price movement as a target
    df['Target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

    return df.dropna()

# 3. Prepare Data
def prepare_data(df):
    features = ['RSI_14', 'SMA_50', 'SMA_200', 'Upper_Band', 'Lower_Band', 'OBV', 'Momentum', 'Lag_1', 'Lag_2', 'Lag_3',
                'US10Y', 'DXY', 'WTI', 'Gold', 'VIX']

    X = df[features]
    y = df['Target']

    # Split and scale
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

# 4. Define and Tune Models
def hyperparameter_tuning():
    param_grid_rf = {'n_estimators': [50, 100], 'max_depth': [5, 10], 'min_samples_split': [2, 5]}
    param_grid_xgb = {'n_estimators': [50, 100], 'max_depth': [3, 6], 'learning_rate': [0.01, 0.1]}
    param_grid_lgb = {'n_estimators': [50, 100], 'num_leaves': [31, 63], 'learning_rate': [0.01, 0.1]}

    rf = GridSearchCV(RandomForestClassifier(), param_grid_rf, cv=3, scoring='accuracy')
    xgb = GridSearchCV(XGBClassifier(), param_grid_xgb, cv=3, scoring='accuracy')
    lgb = GridSearchCV(LGBMClassifier(), param_grid_lgb, cv=3, scoring='accuracy')

    return rf, xgb, lgb

# Stacking
def define_stacking_model():
    base_models = [('rf', RandomForestClassifier()), ('xgb', XGBClassifier()), ('lgb', LGBMClassifier())]
    meta_model = LogisticRegression()
    stacking_model = StackingClassifier(estimators=base_models, final_estimator=meta_model)

    return stacking_model

# 5. Backtest Strategy
def backtest_trades(df, predictions, profit_target=0.01, stop_loss=0.01):
    trades = []
    for i in range(0, len(predictions), 30):  # Every 30 minutes
        if predictions[i] == 1:  # Buy signal
            buy_price = df['Close'].iloc[i]
            trade_success = False
            for j in range(i + 1, len(df)):
                current_price = df['Close'].iloc[j]
                price_change = (current_price - buy_price) / buy_price

                # Logging the time of the trade for further analysis
                trade_time = df.index[i]
                print(f"Trade at {trade_time}: Buy at {buy_price:.2f}, Current Price: {current_price:.2f}, Change: {price_change:.2%}")

                # Check for TP or SL
                if price_change >= profit_target:
                    trades.append((buy_price, current_price, 'profit'))
                    trade_success = True
                    break
                elif price_change <= -stop_loss:
                    trades.append((buy_price, current_price, 'stop_loss'))
                    trade_success = True
                    break

            # If no take profit or stop loss hit, record the result at the end of the timeframe
            if not trade_success:
                trades.append((buy_price, df['Close'].iloc[j], 'no_action'))

    return trades

# 6. Evaluate Models
def train_evaluate_and_backtest(models, X_train, X_test, y_train, y_test, df):
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        print(f"{name} - Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F1: {f1:.2f}")

        # Backtest strategy
        trades = backtest_trades(df[-len(y_test):], y_pred)
        print(f"{name} - Successful Trades: {len([t for t in trades if t[2] == 'profit'])}, "
              f"Loss Trades: {len([t for t in trades if t[2] == 'stop_loss'])}")

# 7. Main Execution
df = load_data()
macro_df = load_macroeconomic_data()
df = add_technical_indicators(df, macro_df)
X_train, X_test, y_train, y_test = prepare_data(df)

# Hyperparameter tuning and stacking
rf, xgb, lgb = hyperparameter_tuning()
stacking_model = define_stacking_model()

#Fit the GridSearchCV object
rf.fit(X_train, y_train)
xgb.fit(X_train, y_train)
lgb.fit(X_train, y_train)

stacking_model = define_stacking_model()

# Train and backtest models
models = {
    "Random Forest": rf.best_estimator_,
    "XGBoost": xgb.best_estimator_,
    "LightGBM": lgb.best_estimator_,
    "Stacking": stacking_model
}

train_evaluate_and_backtest(models, X_train, X_test, y_train, y_test, df)
