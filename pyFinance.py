import yfinance as yf
import plotly.graph_objs as plt

#tsla = yf.Ticker('TSLA')   
#print(tsla)
#print(tsla.info)
#data = yf.download(tickers='TSLA', period='1d', interval='1m')
#print(data)

data = yf.download(tickers='TSLA', period='1d', interval='1m')
#print(data)

fig = plt.Figure(data=[plt.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'TESLA Live Market Data')])

###OPTIONAL
fig.update_layout(
    title='TESLA Live Market Data',
    yaxis_title='Stock Price in $')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=20, label="30m", step="minute", stepmode="backward"),
            dict(count=1, label="1h", step="hour", stepmode="backward"),
            dict(count=4, label="4h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig.show()
