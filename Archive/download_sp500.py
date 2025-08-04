import pandas as pd
import yfinance as yf
from fredapi import Fred

# sp500 = yf.download('^GSPC', start='2000-01-01', progress=True)

# sp500.to_csv('sp500_data.csv')

#Fred API Key (don't share publicly)
fred = Fred(api_key='9357b21a793f849a3ef134b4aab0d7a1')

sp_data = fred.get_series('SP500',observation_start='2000-01-01')

print(sp_data)



