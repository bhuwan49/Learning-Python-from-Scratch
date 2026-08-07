import numpy as np
import pandas as pd
import streamlit as st
import data_extrc
import processrr
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf
import plotly.graph_objects as go

st.title('Capital Asset Pricing Model (CAPM)')
st.write('This app calculates the expected return of a portfolio  using the Capital Asset Pricing Model (CAPM).')
tickit_input = st.text_input('Enter the tickers of the stocks in your portfolio separated by commas (e.g. AAPL,MSFT,GOOGL):')
start_date = st.date_input('Enter the start date:')
end_date = st.date_input('Enter the end date:')
if st.button('Get Data'):
    try:
        data = data_extrc.fetching_data(tickit_input, start_date, end_date)
    except Exception as e:
        st.error(f'Could not fetch data: {e}')
        st.stop()
    st.write(f'Data from {start_date} to {end_date}')
    st.table(data.head())
    normalized_data = data_extrc.Normalizing(data)
    st.plotly_chart(processrr.interative_plot(normalized_data, 'Normalized Prices'), width='stretch')

    # Calculate beta and alpha of all stocks
    stocks_daily_return = data_extrc.daily_return(data)
    beta, alpha = processrr.calculate_beta_alpha(stocks_daily_return)
    if not beta:
        st.error('No valid stock data found. Please check the tickers and date range.')
        st.stop()

    # Annualized market return (S&P500), in decimal
    rm = stocks_daily_return['sp500'].mean() * 252 / 100
    st.header('Market Return (RM) Sp500:')
    st.subheader(f'{rm * 100:.2f}%')
    st.write('The CAPM formula is:')
    st.latex(r'ER_i = R_f + \beta_i(ER_m - R_f)')

    # Risk-free rate from the 10-year Treasury yield (^TNX), converted to decimal
    rf_raw = yf.download('^TNX', start=start_date, end=end_date, auto_adjust=False, progress=False)['Adj Close']
    if isinstance(rf_raw, pd.DataFrame):
        rf_raw = rf_raw.iloc[:, 0]
    rf = float(rf_raw.mean()) / 100
    st.subheader('Risk-Free Rate (Rf):')
    st.write(f'{rf * 100:.2f}%')

    keys = list(beta.keys())
    ER = {}
    for i in keys:
        ER[i] = rf + (beta[i] * (rm - rf))
    for i in keys:
        st.write('Expected Return Based on CAPM for {} is {:.2f}%'.format(i, ER[i] * 100))

    fig = go.Figure([go.Bar(x=list(beta.keys()), y=list(beta.values()))])
    fig.update_layout(title_text='Beta Values for Stocks', xaxis_title='Stock Tickers',
                      yaxis_title='Beta Values', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, width='stretch')

    # Alpha values
    st.subheader('Alpha Values for Stocks')
    fig = go.Figure([go.Bar(x=list(alpha.keys()), y=list(alpha.values()))])
    fig.update_layout(title_text='Alpha Values for Stocks', xaxis_title='Stock Tickers',
                      yaxis_title='Alpha Values', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, width='stretch')

    # Portfolio weights
    st.subheader('Portfolio Weights')
    st.write('assuming equal weights for all stocks')
    portfolio_weights = np.ones(len(keys)) / len(keys)
    portfolio_return = float(np.dot(list(ER.values()), portfolio_weights))
    st.write('Expected Return Based on CAPM for Portfolio is {:.2f}%'.format(portfolio_return * 100))

    # Plot of portfolio return and market return
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(ER.keys()), y=[v * 100 for v in ER.values()], mode='lines+markers', name='Expected Return'))
    fig.add_trace(go.Scatter(x=list(ER.keys()), y=[rm * 100] * len(ER), mode='lines', name='Market Return'))
    fig.update_layout(title_text='Portfolio Return vs Market Return', xaxis_title='Stock Tickers',
                      yaxis_title='Return (%)', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, width='stretch')

    # Pie chart of total portfolio return and market return
    fig = px.pie(values=[portfolio_return * 100, rm * 100], names=['Portfolio Return', 'Market Return'],
                 title='Portfolio Return vs Market Return')
    st.plotly_chart(fig, width='stretch')

    # Table of returns, alpha and beta
    Returns = pd.DataFrame({'Return': {i: ER[i] * 100 for i in keys}})
    Returns = Returns.sort_values(by='Return', ascending=False)
    st.subheader('Returns')
    fig = go.Figure([go.Bar(x=Returns.index, y=Returns['Return'])])
    fig.update_layout(title_text='Returns for Stocks', xaxis_title='Stock Tickers',
                      yaxis_title='Return (%)', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, width='stretch')

    st.subheader('Returns, Alpha and Beta')
    Returns['Alpha'] = [alpha[i] for i in Returns.index]
    Returns['Beta'] = [beta[i] for i in Returns.index]
    st.table(Returns)