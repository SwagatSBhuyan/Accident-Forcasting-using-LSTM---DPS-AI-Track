import numpy as np
from sklearn import metrics

def timeSeriesMultivariate(dataset, target, start, end, window, horizon):
    X = []
    y = []
    start = start + window
    if end is None:
        end = len(dataset) - horizon
    for i in range(start, end):
        indices = range(i-window, i)
        X.append(dataset[indices])
        indicey = range(i+1, i+1+horizon)
        y.append(target[indicey])
    return np.array(X), np.array(y) 

def timeSeriesEvaluationMetrics(y_true, y_pred):
    print("\n=============================================================\n")
    print('Time Series Evaluation metric scores: ')
    print(f'MSE: {metrics.mean_squared_error(y_true, y_pred)}')
    print(f'MAE: {metrics.mean_absolute_error(y_true, y_pred)}')
    print(f'RMSE: {np.sqrt(metrics.mean_squared_error(y_true, y_pred))}')
    print(f'R2: {metrics.r2_score(y_true, y_pred)}') 
    print("=============================================================\n\n")