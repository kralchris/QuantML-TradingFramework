# Machine Learning-Driven Algo Quantitative Trading Strategy with Systematic Market Prediction Framework

## Overview
This project showcases a robust quantitative trading framework using machine learning classification models and technical indicators to predict US stock index movements. Combining historical market and macroeconomic data, this framework aims to develop and backtest trading strategies that dynamically respond to evolving market conditions.

## Objectives
- **Data Acquisition**: Retrieve and process market data for the NASDAQ-100 (US100) along with key macroeconomic indicators, such as US Treasury Yield, Dollar Index, WTI Crude Oil, Gold, and VIX.
- **Feature Engineering**: Implement technical indicators like RSI, Moving Averages, Bollinger Bands, On-Balance Volume (OBV), and Momentum to capture underlying market trends and momentum.
- **Modeling and Tuning**: Apply and optimize machine learning models, including Random Forest, XGBoost, LightGBM, and a Stacking Classifier, to predict market directions.
- **Backtesting Strategy**: Evaluate the profitability of model-generated trading signals using historical data for realistic assessment and validation.

## Project Components

### 1. Market Data Collection
The `load_data` function leverages `yfinance` to pull historical daily market data for NASDAQ-100, and `load_macroeconomic_data` integrates relevant macroeconomic indicators, broadening the data landscape for analysis.

### 2. Technical Indicator Calculation
The `add_technical_indicators` function computes indicators like RSI, Bollinger Bands, Moving Averages, and OBV, enhancing the data’s interpretability and its predictive value in machine learning models.

### 3. Data Preparation
Using the `prepare_data` function, the data is organized into model-ready features and target variables, including lagged features and normalized metrics for efficient training and evaluation.

### 4. Model Selection & Tuning
The `hyperparameter_tuning` function fine-tunes hyperparameters for models such as Random Forest, XGBoost, and LightGBM. The Stacking Classifier, defined in `define_stacking_model`, serves as an ensemble to aggregate model strengths for robust predictions.

### 5. Backtesting Strategy
The `backtest_trades` function incorporates a profit-target and stop-loss strategy to simulate real-world trading conditions, assessing profitability based on model predictions over historical data.

### 6. Model Evaluation & Performance Metrics
The `train_evaluate_and_backtest` function calculates performance metrics, such as accuracy, precision, recall, and F1 score, for each model. Additionally, backtesting results provide insights into trade outcomes (successful, loss, or no action), aligning model performance with market relevance.

### Sample Model Output
Detailed outputs from each model provide insight into model behavior and backtesting results:

- **Random Forest**: 
    - **Accuracy**: 0.48
    - **Precision**: 0.59
    - **Recall**: 0.27
    - **F1**: 0.37
    - **Backtesting**: 5 successful trades, 4 loss trades

- **XGBoost**: 
    - **Accuracy**: 0.54
    - **Precision**: 0.57
    - **Recall**: 0.76
    - **F1**: 0.65
    - **Backtesting**: 19 successful trades, 11 loss trades

- **LightGBM**: 
    - **Accuracy**: 0.53
    - **Precision**: 0.58
    - **Recall**: 0.59
    - **F1**: 0.58
    - **Backtesting**: 18 successful trades, 12 loss trades

- **Stacking Classifier**: 
    - **Accuracy**: 0.56
    - **Precision**: 0.56
    - **Recall**: 1.00
    - **F1**: 0.72
    - **Backtesting**: 25 successful trades, 16 loss trades

This output demonstrates the effectiveness of each model under historical data conditions, aiding in selecting optimal models for real-world application.

## Conclusion
This quantitative trading framework highlights the synergy between machine learning and financial markets, where feature engineering, model tuning, and backtesting coalesce to form a foundational strategy for systematic trading.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

# Output:

```[*********************100%***********************]  1 of 1 completed
[*********************100%***********************]  1 of 1 completed
[*********************100%***********************]  1 of 1 completed
[*********************100%***********************]  1 of 1 completed
[*********************100%***********************]  1 of 1 completed
[*********************100%***********************]  1 of 1 completed
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000233 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.000846 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.000759 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.000819 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000249 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.000818 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000264 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.000899 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000244 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000236 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000239 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000254 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000266 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.000801 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000243 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.000836 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000272 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000206 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000253 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000202 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000237 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.000928 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000243 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 1740, number of negative: 1492
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000254 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3232, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 2610, number of negative: 2238
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000289 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 4848, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
Random Forest - Accuracy: 0.48, Precision: 0.59, Recall: 0.27, F1: 0.37
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8354.29, Change: -0.10%
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8402.61, Change: 0.48%
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8466.89, Change: 1.25%
Trade at 2020-03-06 00:00:00: Buy at 8530.34, Current Price: 7948.03, Change: -6.83%
Trade at 2020-04-20 00:00:00: Buy at 8726.51, Current Price: 8403.00, Change: -3.71%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9704.69, Change: 0.49%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9629.66, Change: -0.29%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9824.39, Change: 1.73%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10626.46, Change: -0.70%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10645.22, Change: -0.53%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10952.08, Change: 2.34%
Trade at 2020-10-08 00:00:00: Buy at 11550.94, Current Price: 11725.85, Change: 1.51%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 11906.44, Change: -0.66%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 11905.94, Change: -0.66%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 12079.81, Change: 0.79%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 12152.22, Change: 1.39%
Trade at 2021-02-18 00:00:00: Buy at 13637.51, Current Price: 13580.78, Change: -0.42%
Trade at 2021-02-18 00:00:00: Buy at 13637.51, Current Price: 13223.74, Change: -3.03%
Trade at 2021-12-16 00:00:00: Buy at 15863.94, Current Price: 15801.46, Change: -0.39%
Trade at 2021-12-16 00:00:00: Buy at 15863.94, Current Price: 15627.64, Change: -1.49%
Random Forest - Successful Trades: 5, Loss Trades: 4
XGBoost - Accuracy: 0.54, Precision: 0.57, Recall: 0.76, F1: 0.65
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8354.29, Change: -0.10%
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8402.61, Change: 0.48%
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8466.89, Change: 1.25%
Trade at 2020-01-23 00:00:00: Buy at 9216.98, Current Price: 9141.47, Change: -0.82%
Trade at 2020-01-23 00:00:00: Buy at 9216.98, Current Price: 8952.18, Change: -2.87%
Trade at 2020-03-06 00:00:00: Buy at 8530.34, Current Price: 7948.03, Change: -6.83%
Trade at 2020-04-20 00:00:00: Buy at 8726.51, Current Price: 8403.00, Change: -3.71%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9704.69, Change: 0.49%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9629.66, Change: -0.29%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9824.39, Change: 1.73%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10626.46, Change: -0.70%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10645.22, Change: -0.53%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10952.08, Change: 2.34%
Trade at 2020-08-26 00:00:00: Buy at 11971.94, Current Price: 11926.16, Change: -0.38%
Trade at 2020-08-26 00:00:00: Buy at 11971.94, Current Price: 11995.85, Change: 0.20%
Trade at 2020-08-26 00:00:00: Buy at 11971.94, Current Price: 12110.70, Change: 1.16%
Trade at 2020-10-08 00:00:00: Buy at 11550.94, Current Price: 11725.85, Change: 1.51%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 11906.44, Change: -0.66%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 11905.94, Change: -0.66%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 12079.81, Change: 0.79%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 12152.22, Change: 1.39%
Trade at 2021-01-05 00:00:00: Buy at 12802.38, Current Price: 12623.35, Change: -1.40%
Trade at 2021-02-18 00:00:00: Buy at 13637.51, Current Price: 13580.78, Change: -0.42%
Trade at 2021-02-18 00:00:00: Buy at 13637.51, Current Price: 13223.74, Change: -3.03%
Trade at 2021-04-01 00:00:00: Buy at 13329.52, Current Price: 13598.16, Change: 2.02%
Trade at 2021-05-14 00:00:00: Buy at 13393.12, Current Price: 13312.91, Change: -0.60%
Trade at 2021-05-14 00:00:00: Buy at 13393.12, Current Price: 13217.68, Change: -1.31%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14572.75, Change: 0.33%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14554.80, Change: 0.21%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14560.05, Change: 0.24%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14727.63, Change: 1.40%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15027.76, Change: -0.17%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15088.98, Change: 0.24%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15136.68, Change: 0.55%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15140.77, Change: 0.58%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15002.83, Change: -0.34%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 14857.92, Change: -1.30%
Trade at 2021-09-22 00:00:00: Buy at 15176.51, Current Price: 15316.58, Change: 0.92%
Trade at 2021-09-22 00:00:00: Buy at 15176.51, Current Price: 15329.68, Change: 1.01%
Trade at 2021-11-03 00:00:00: Buy at 16144.50, Current Price: 16346.24, Change: 1.25%
Trade at 2021-12-16 00:00:00: Buy at 15863.94, Current Price: 15801.46, Change: -0.39%
Trade at 2021-12-16 00:00:00: Buy at 15863.94, Current Price: 15627.64, Change: -1.49%
Trade at 2022-01-31 00:00:00: Buy at 14930.05, Current Price: 15019.68, Change: 0.60%
Trade at 2022-01-31 00:00:00: Buy at 14930.05, Current Price: 15139.74, Change: 1.40%
Trade at 2022-03-15 00:00:00: Buy at 13458.56, Current Price: 13956.79, Change: 3.70%
Trade at 2022-07-25 00:00:00: Buy at 12328.41, Current Price: 12086.90, Change: -1.96%
Trade at 2022-09-06 00:00:00: Buy at 12011.31, Current Price: 12259.39, Change: 2.07%
Trade at 2022-10-18 00:00:00: Buy at 11147.74, Current Price: 11103.38, Change: -0.40%
Trade at 2022-10-18 00:00:00: Buy at 11147.74, Current Price: 11046.71, Change: -0.91%
Trade at 2022-10-18 00:00:00: Buy at 11147.74, Current Price: 11310.33, Change: 1.46%
Trade at 2022-11-30 00:00:00: Buy at 12030.06, Current Price: 12041.89, Change: 0.10%
Trade at 2022-11-30 00:00:00: Buy at 12030.06, Current Price: 11994.26, Change: -0.30%
Trade at 2022-11-30 00:00:00: Buy at 12030.06, Current Price: 11786.80, Change: -2.02%
Trade at 2023-01-13 00:00:00: Buy at 11541.48, Current Price: 11557.19, Change: 0.14%
Trade at 2023-01-13 00:00:00: Buy at 11541.48, Current Price: 11410.29, Change: -1.14%
Trade at 2023-07-10 00:00:00: Buy at 15045.64, Current Price: 15119.06, Change: 0.49%
Trade at 2023-07-10 00:00:00: Buy at 15045.64, Current Price: 15307.23, Change: 1.74%
Trade at 2023-08-21 00:00:00: Buy at 14936.69, Current Price: 14908.96, Change: -0.19%
Trade at 2023-08-21 00:00:00: Buy at 14936.69, Current Price: 15148.06, Change: 1.42%
Trade at 2023-10-03 00:00:00: Buy at 14565.62, Current Price: 14776.25, Change: 1.45%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 15817.18, Change: 0.03%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 15833.17, Change: 0.13%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 15837.99, Change: 0.16%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 16027.06, Change: 1.36%
Trade at 2024-09-17 00:00:00: Buy at 19432.40, Current Price: 19344.49, Change: -0.45%
Trade at 2024-09-17 00:00:00: Buy at 19432.40, Current Price: 19839.83, Change: 2.10%
XGBoost - Successful Trades: 19, Loss Trades: 11
[LightGBM] [Info] Number of positive: 2610, number of negative: 2238
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000287 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 4848, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
LightGBM - Accuracy: 0.53, Precision: 0.58, Recall: 0.59, F1: 0.58
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8354.29, Change: -0.10%
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8402.61, Change: 0.48%
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8466.89, Change: 1.25%
Trade at 2020-01-23 00:00:00: Buy at 9216.98, Current Price: 9141.47, Change: -0.82%
Trade at 2020-01-23 00:00:00: Buy at 9216.98, Current Price: 8952.18, Change: -2.87%
Trade at 2020-03-06 00:00:00: Buy at 8530.34, Current Price: 7948.03, Change: -6.83%
Trade at 2020-04-20 00:00:00: Buy at 8726.51, Current Price: 8403.00, Change: -3.71%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9704.69, Change: 0.49%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9629.66, Change: -0.29%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9824.39, Change: 1.73%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10626.46, Change: -0.70%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10645.22, Change: -0.53%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10952.08, Change: 2.34%
Trade at 2020-08-26 00:00:00: Buy at 11971.94, Current Price: 11926.16, Change: -0.38%
Trade at 2020-08-26 00:00:00: Buy at 11971.94, Current Price: 11995.85, Change: 0.20%
Trade at 2020-08-26 00:00:00: Buy at 11971.94, Current Price: 12110.70, Change: 1.16%
Trade at 2020-10-08 00:00:00: Buy at 11550.94, Current Price: 11725.85, Change: 1.51%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 11906.44, Change: -0.66%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 11905.94, Change: -0.66%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 12079.81, Change: 0.79%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 12152.22, Change: 1.39%
Trade at 2021-01-05 00:00:00: Buy at 12802.38, Current Price: 12623.35, Change: -1.40%
Trade at 2021-02-18 00:00:00: Buy at 13637.51, Current Price: 13580.78, Change: -0.42%
Trade at 2021-02-18 00:00:00: Buy at 13637.51, Current Price: 13223.74, Change: -3.03%
Trade at 2021-04-01 00:00:00: Buy at 13329.52, Current Price: 13598.16, Change: 2.02%
Trade at 2021-05-14 00:00:00: Buy at 13393.12, Current Price: 13312.91, Change: -0.60%
Trade at 2021-05-14 00:00:00: Buy at 13393.12, Current Price: 13217.68, Change: -1.31%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14572.75, Change: 0.33%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14554.80, Change: 0.21%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14560.05, Change: 0.24%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14727.63, Change: 1.40%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15027.76, Change: -0.17%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15088.98, Change: 0.24%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15136.68, Change: 0.55%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15140.77, Change: 0.58%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15002.83, Change: -0.34%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 14857.92, Change: -1.30%
Trade at 2021-09-22 00:00:00: Buy at 15176.51, Current Price: 15316.58, Change: 0.92%
Trade at 2021-09-22 00:00:00: Buy at 15176.51, Current Price: 15329.68, Change: 1.01%
Trade at 2021-11-03 00:00:00: Buy at 16144.50, Current Price: 16346.24, Change: 1.25%
Trade at 2021-12-16 00:00:00: Buy at 15863.94, Current Price: 15801.46, Change: -0.39%
Trade at 2021-12-16 00:00:00: Buy at 15863.94, Current Price: 15627.64, Change: -1.49%
Trade at 2022-03-15 00:00:00: Buy at 13458.56, Current Price: 13956.79, Change: 3.70%
Trade at 2022-04-27 00:00:00: Buy at 13003.36, Current Price: 13456.06, Change: 3.48%
Trade at 2022-07-25 00:00:00: Buy at 12328.41, Current Price: 12086.90, Change: -1.96%
Trade at 2022-09-06 00:00:00: Buy at 12011.31, Current Price: 12259.39, Change: 2.07%
Trade at 2023-01-13 00:00:00: Buy at 11541.48, Current Price: 11557.19, Change: 0.14%
Trade at 2023-01-13 00:00:00: Buy at 11541.48, Current Price: 11410.29, Change: -1.14%
Trade at 2023-02-28 00:00:00: Buy at 12042.12, Current Price: 11938.57, Change: -0.86%
Trade at 2023-02-28 00:00:00: Buy at 12042.12, Current Price: 12044.87, Change: 0.02%
Trade at 2023-02-28 00:00:00: Buy at 12042.12, Current Price: 12290.81, Change: 2.07%
Trade at 2023-05-24 00:00:00: Buy at 13604.48, Current Price: 13938.53, Change: 2.46%
Trade at 2023-10-03 00:00:00: Buy at 14565.62, Current Price: 14776.25, Change: 1.45%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 15817.18, Change: 0.03%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 15833.17, Change: 0.13%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 15837.99, Change: 0.16%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 16027.06, Change: 1.36%
Trade at 2023-12-28 00:00:00: Buy at 16898.47, Current Price: 16825.93, Change: -0.43%
Trade at 2023-12-28 00:00:00: Buy at 16898.47, Current Price: 16543.94, Change: -2.10%
Trade at 2024-05-08 00:00:00: Buy at 18085.01, Current Price: 18113.46, Change: 0.16%
Trade at 2024-05-08 00:00:00: Buy at 18085.01, Current Price: 18161.18, Change: 0.42%
Trade at 2024-05-08 00:00:00: Buy at 18085.01, Current Price: 18198.61, Change: 0.63%
Trade at 2024-05-08 00:00:00: Buy at 18085.01, Current Price: 18322.77, Change: 1.31%
Trade at 2024-06-21 00:00:00: Buy at 19700.43, Current Price: 19474.62, Change: -1.15%
LightGBM - Successful Trades: 18, Loss Trades: 12
[LightGBM] [Info] Number of positive: 2610, number of negative: 2238
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000332 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 4848, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538366 -> initscore=0.153768
[LightGBM] [Info] Start training from score 0.153768
[LightGBM] [Info] Number of positive: 2088, number of negative: 1790
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000259 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3878, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538422 -> initscore=0.153991
[LightGBM] [Info] Start training from score 0.153991
[LightGBM] [Info] Number of positive: 2088, number of negative: 1790
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.001027 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3878, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538422 -> initscore=0.153991
[LightGBM] [Info] Start training from score 0.153991
[LightGBM] [Info] Number of positive: 2088, number of negative: 1790
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000258 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3878, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538422 -> initscore=0.153991
[LightGBM] [Info] Start training from score 0.153991
[LightGBM] [Info] Number of positive: 2088, number of negative: 1791
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.000995 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3879, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538283 -> initscore=0.153433
[LightGBM] [Info] Start training from score 0.153433
[LightGBM] [Info] Number of positive: 2088, number of negative: 1791
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.001130 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3825
[LightGBM] [Info] Number of data points in the train set: 3879, number of used features: 15
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.538283 -> initscore=0.153433
[LightGBM] [Info] Start training from score 0.153433
Stacking - Accuracy: 0.56, Precision: 0.56, Recall: 1.00, F1: 0.72
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8354.29, Change: -0.10%
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8402.61, Change: 0.48%
Trade at 2019-12-09 00:00:00: Buy at 8362.74, Current Price: 8466.89, Change: 1.25%
Trade at 2020-01-23 00:00:00: Buy at 9216.98, Current Price: 9141.47, Change: -0.82%
Trade at 2020-01-23 00:00:00: Buy at 9216.98, Current Price: 8952.18, Change: -2.87%
Trade at 2020-03-06 00:00:00: Buy at 8530.34, Current Price: 7948.03, Change: -6.83%
Trade at 2020-04-20 00:00:00: Buy at 8726.51, Current Price: 8403.00, Change: -3.71%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9704.69, Change: 0.49%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9629.66, Change: -0.29%
Trade at 2020-06-02 00:00:00: Buy at 9657.31, Current Price: 9824.39, Change: 1.73%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10626.46, Change: -0.70%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10645.22, Change: -0.53%
Trade at 2020-07-15 00:00:00: Buy at 10701.68, Current Price: 10952.08, Change: 2.34%
Trade at 2020-08-26 00:00:00: Buy at 11971.94, Current Price: 11926.16, Change: -0.38%
Trade at 2020-08-26 00:00:00: Buy at 11971.94, Current Price: 11995.85, Change: 0.20%
Trade at 2020-08-26 00:00:00: Buy at 11971.94, Current Price: 12110.70, Change: 1.16%
Trade at 2020-10-08 00:00:00: Buy at 11550.94, Current Price: 11725.85, Change: 1.51%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 11906.44, Change: -0.66%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 11905.94, Change: -0.66%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 12079.81, Change: 0.79%
Trade at 2020-11-19 00:00:00: Buy at 11985.43, Current Price: 12152.22, Change: 1.39%
Trade at 2021-01-05 00:00:00: Buy at 12802.38, Current Price: 12623.35, Change: -1.40%
Trade at 2021-02-18 00:00:00: Buy at 13637.51, Current Price: 13580.78, Change: -0.42%
Trade at 2021-02-18 00:00:00: Buy at 13637.51, Current Price: 13223.74, Change: -3.03%
Trade at 2021-04-01 00:00:00: Buy at 13329.52, Current Price: 13598.16, Change: 2.02%
Trade at 2021-05-14 00:00:00: Buy at 13393.12, Current Price: 13312.91, Change: -0.60%
Trade at 2021-05-14 00:00:00: Buy at 13393.12, Current Price: 13217.68, Change: -1.31%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14572.75, Change: 0.33%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14554.80, Change: 0.21%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14560.05, Change: 0.24%
Trade at 2021-06-28 00:00:00: Buy at 14524.98, Current Price: 14727.63, Change: 1.40%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15027.76, Change: -0.17%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15088.98, Change: 0.24%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15136.68, Change: 0.55%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15140.77, Change: 0.58%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 15002.83, Change: -0.34%
Trade at 2021-08-10 00:00:00: Buy at 15053.58, Current Price: 14857.92, Change: -1.30%
Trade at 2021-09-22 00:00:00: Buy at 15176.51, Current Price: 15316.58, Change: 0.92%
Trade at 2021-09-22 00:00:00: Buy at 15176.51, Current Price: 15329.68, Change: 1.01%
Trade at 2021-11-03 00:00:00: Buy at 16144.50, Current Price: 16346.24, Change: 1.25%
Trade at 2021-12-16 00:00:00: Buy at 15863.94, Current Price: 15801.46, Change: -0.39%
Trade at 2021-12-16 00:00:00: Buy at 15863.94, Current Price: 15627.64, Change: -1.49%
Trade at 2022-01-31 00:00:00: Buy at 14930.05, Current Price: 15019.68, Change: 0.60%
Trade at 2022-01-31 00:00:00: Buy at 14930.05, Current Price: 15139.74, Change: 1.40%
Trade at 2022-03-15 00:00:00: Buy at 13458.56, Current Price: 13956.79, Change: 3.70%
Trade at 2022-04-27 00:00:00: Buy at 13003.36, Current Price: 13456.06, Change: 3.48%
Trade at 2022-06-09 00:00:00: Buy at 12269.78, Current Price: 11832.82, Change: -3.56%
Trade at 2022-07-25 00:00:00: Buy at 12328.41, Current Price: 12086.90, Change: -1.96%
Trade at 2022-09-06 00:00:00: Buy at 12011.31, Current Price: 12259.39, Change: 2.07%
Trade at 2022-10-18 00:00:00: Buy at 11147.74, Current Price: 11103.38, Change: -0.40%
Trade at 2022-10-18 00:00:00: Buy at 11147.74, Current Price: 11046.71, Change: -0.91%
Trade at 2022-10-18 00:00:00: Buy at 11147.74, Current Price: 11310.33, Change: 1.46%
Trade at 2022-11-30 00:00:00: Buy at 12030.06, Current Price: 12041.89, Change: 0.10%
Trade at 2022-11-30 00:00:00: Buy at 12030.06, Current Price: 11994.26, Change: -0.30%
Trade at 2022-11-30 00:00:00: Buy at 12030.06, Current Price: 11786.80, Change: -2.02%
Trade at 2023-01-13 00:00:00: Buy at 11541.48, Current Price: 11557.19, Change: 0.14%
Trade at 2023-01-13 00:00:00: Buy at 11541.48, Current Price: 11410.29, Change: -1.14%
Trade at 2023-02-28 00:00:00: Buy at 12042.12, Current Price: 11938.57, Change: -0.86%
Trade at 2023-02-28 00:00:00: Buy at 12042.12, Current Price: 12044.87, Change: 0.02%
Trade at 2023-02-28 00:00:00: Buy at 12042.12, Current Price: 12290.81, Change: 2.07%
Trade at 2023-04-12 00:00:00: Buy at 12848.35, Current Price: 13109.39, Change: 2.03%
Trade at 2023-05-24 00:00:00: Buy at 13604.48, Current Price: 13938.53, Change: 2.46%
Trade at 2023-07-10 00:00:00: Buy at 15045.64, Current Price: 15119.06, Change: 0.49%
Trade at 2023-07-10 00:00:00: Buy at 15045.64, Current Price: 15307.23, Change: 1.74%
Trade at 2023-08-21 00:00:00: Buy at 14936.69, Current Price: 14908.96, Change: -0.19%
Trade at 2023-08-21 00:00:00: Buy at 14936.69, Current Price: 15148.06, Change: 1.42%
Trade at 2023-10-03 00:00:00: Buy at 14565.62, Current Price: 14776.25, Change: 1.45%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 15817.18, Change: 0.03%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 15833.17, Change: 0.13%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 15837.99, Change: 0.16%
Trade at 2023-11-14 00:00:00: Buy at 15812.47, Current Price: 16027.06, Change: 1.36%
Trade at 2023-12-28 00:00:00: Buy at 16898.47, Current Price: 16825.93, Change: -0.43%
Trade at 2023-12-28 00:00:00: Buy at 16898.47, Current Price: 16543.94, Change: -2.10%
Trade at 2024-02-12 00:00:00: Buy at 17882.66, Current Price: 17600.42, Change: -1.58%
Trade at 2024-03-26 00:00:00: Buy at 18210.54, Current Price: 18280.84, Change: 0.39%
Trade at 2024-03-26 00:00:00: Buy at 18210.54, Current Price: 18254.69, Change: 0.24%
Trade at 2024-03-26 00:00:00: Buy at 18210.54, Current Price: 18293.20, Change: 0.45%
Trade at 2024-03-26 00:00:00: Buy at 18210.54, Current Price: 18121.78, Change: -0.49%
Trade at 2024-03-26 00:00:00: Buy at 18210.54, Current Price: 18160.19, Change: -0.28%
Trade at 2024-03-26 00:00:00: Buy at 18210.54, Current Price: 17878.78, Change: -1.82%
Trade at 2024-05-08 00:00:00: Buy at 18085.01, Current Price: 18113.46, Change: 0.16%
Trade at 2024-05-08 00:00:00: Buy at 18085.01, Current Price: 18161.18, Change: 0.42%
Trade at 2024-05-08 00:00:00: Buy at 18085.01, Current Price: 18198.61, Change: 0.63%
Trade at 2024-05-08 00:00:00: Buy at 18085.01, Current Price: 18322.77, Change: 1.31%
Trade at 2024-06-21 00:00:00: Buy at 19700.43, Current Price: 19474.62, Change: -1.15%
Trade at 2024-08-05 00:00:00: Buy at 17895.16, Current Price: 18077.92, Change: 1.02%
Trade at 2024-09-17 00:00:00: Buy at 19432.40, Current Price: 19344.49, Change: -0.45%
Trade at 2024-09-17 00:00:00: Buy at 19432.40, Current Price: 19839.83, Change: 2.10%
Stacking - Successful Trades: 25, Loss Trades: 16```
