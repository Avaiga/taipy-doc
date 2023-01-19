import time
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def train(historical_daily_temperature: pd.DataFrame):
    print('----- Started training -----')
    # Simulate the training process
    for epoch in range(2):
        time.sleep(0.5)
        print(f'Epoch {epoch} ...')
    return ARIMA(endog=historical_daily_temperature['Temp'].to_numpy(), order=(1, 1, 0)).fit()
