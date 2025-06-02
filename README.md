# 📈 Stock Price Prediction App

A simple and interactive Streamlit web app that allows users to visualize historical stock data, apply a 7-day moving average, and predict future stock prices using Linear Regression.

## 🚀 Features

- 🔍 Fetches historical stock data using Yahoo Finance
- 📊 Plots stock price and 7-day moving average
- 🤖 Predicts future prices using a linear regression model
- 📈 Displays actual vs. predicted prices in a line chart
- ⚡ Clean and responsive UI built with Streamlit

## 🧠 How It Works

The app uses the **7-day moving average** of the closing price as input to a **linear regression** model, which predicts the next day's stock price.

## 📦 Tech Stack

- Python 🐍
- [Streamlit](https://streamlit.io/) – for building the web app
- [YFinance](https://pypi.org/project/yfinance/) – for pulling stock market data
- Pandas & Matplotlib – for data manipulation and visualization
- Scikit-learn – for linear regression modeling

## 🖥️ Demo

Try the live app here 👉 [streamlit-app-link](https://your-username-stock-price-prediction.streamlit.app) *(replace with your actual link)*

## 📸 Screenshots

![App Screenshot](https://your-screenshot-link.com/preview.png) *(optional)*

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction

2. Install dependencies:

bash
Copy code
pip install -r requirements.txt

3. Run the app:

bash
Copy code
streamlit run app.py

📁 Project Structure
bash
Copy code
├── app.py                  # Main Streamlit app
├── stock_price_prediction.ipynb  # Jupyter notebook for analysis
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
📌 Example Tickers
Try these stock symbols in the app:

AAPL – Apple Inc.

GOOGL – Alphabet Inc.

TSLA – Tesla Inc.

MSFT – Microsoft Corp.

🙋‍♂️ Author
Tedla Tesfaye
Data Science Intern | Aspiring ML Engineer
LinkedIn • GitHub

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

yaml
Copy code
