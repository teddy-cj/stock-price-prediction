import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# App Title
st.set_page_config(page_title="Stock Forecast App", layout="wide")
st.title("📊 Stock Price Forecasting App")

# Sidebar input
st.sidebar.header("Select Stock")
ticker = st.sidebar.text_input("Enter Ticker Symbol (e.g., AAPL, TSLA)", "AAPL").upper().strip()

# Data fetch with spinner
with st.spinner("Fetching data..."):
    data = yf.download(ticker, start="2018-01-01", end="2024-12-31")

# Handle MultiIndex
if isinstance(data.columns, pd.MultiIndex):
    data.columns = ['_'.join(col).strip() for col in data.columns.values]
    close_col = f'Close_{ticker}'
else:
    close_col = 'Close'

if close_col not in data.columns:
    st.error(f"Unable to find closing price column for {ticker}")
    st.stop()

# Compute moving average
data['7_day_MA'] = data[close_col].rolling(window=7).mean()
data.dropna(inplace=True)

# Display quick metrics
latest_price = data[close_col].iloc[-1]
high_52 = data[close_col].max()
low_52 = data[close_col].min()

st.subheader(f"📌 Key Stats for {ticker}")
col1, col2, col3 = st.columns(3)
col1.metric("Latest Close", f"${latest_price:.2f}")
col2.metric("52-Week High", f"${high_52:.2f}")
col3.metric("52-Week Low", f"${low_52:.2f}")

# Show chart
st.subheader("📈 Price Chart with 7-Day Moving Average")
st.line_chart(data[[close_col, '7_day_MA']])

# Regression
X = data[['7_day_MA']]
y = data[close_col].shift(-1).dropna()
X = X.iloc[:-1]

model = LinearRegression()
model.fit(X, y)
pred = model.predict(X)

# Prediction plot
st.subheader("🔮 Predicted vs Actual")
fig, ax = plt.subplots()
ax.plot(y.values, label='Actual', color='blue')
ax.plot(pred, label='Predicted', color='orange', linestyle='--')
ax.set_title("Actual vs Predicted Closing Price")
ax.set_xlabel("Days")
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)
