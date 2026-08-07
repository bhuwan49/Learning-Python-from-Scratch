import numpy as np
import pandas as pd
import yfinance as yf

def fetching_data(tickers_input, start_date, end_date):
    # 1. Properly split the user input string into a list of individual tickers
    tickers = [ticker.strip() for ticker in tickers_input.split(",")]
    # Remove empty and duplicate entries
    tickers = list(dict.fromkeys(t for t in tickers if t))

    if not tickers:
        raise ValueError('No valid tickers provided.')

    # 2. Download stock data forcing 'Adj Close' to be present
    raw_data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=False, progress=False)
    data = raw_data['Adj Close']

    # 3. Modern yfinance fix: If only 1 ticker was typed, convert the Series layout back into a clean DataFrame column
    if isinstance(data, pd.Series):
        data = data.to_frame(name=tickers[0])

    # 4. Download S&P500 market tracking baseline data
    raw_sp500 = yf.download("^GSPC", start=start_date, end=end_date, auto_adjust=False, progress=False)
    sp500_data = raw_sp500['Adj Close']
    # Modern yfinance returns a DataFrame even for a single ticker
    if isinstance(sp500_data, pd.DataFrame):
        sp500_data = sp500_data.iloc[:, 0]

    # 5. Merge the S&P500 data cleanly as a new column
    data = data.join(sp500_data.rename('sp500'))
    data.reset_index(inplace=True)
    return data

def Normalizing(df):
    x = df.copy()
    for i in x.columns[1:]:
        first_valid = x[i].dropna().iloc[0] if not x[i].dropna().empty else np.nan
        x[i] = x[i] / first_valid
    return x

def daily_return(df):
    df_daily_return = df.copy()
    for i in df.columns[1:]:
        df_daily_return[i] = df[i].pct_change(fill_method=None) * 100
    return df_daily_return
