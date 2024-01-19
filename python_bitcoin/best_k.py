import pyupbit
import numpy as np


def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-BTC", count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0005
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod().iloc[-2]
    return ror

ror_list = []
for k in np.arange(0.1, 1.0, 0.01):
    ror_list.append(get_ror(k))

max_value = max(ror_list)
max_index = ror_list.index(max_value)
print(max_index, max_value)