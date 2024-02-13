from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies import Strategy
from lumibot.traders import Trader
from datetime import datetime
from alpaca_trade_api import REST
import pandas as pd
from ta.trend import MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands
from finbert_utils import estimate_sentiment
from datetime import timedelta

API_KEY = "PK52MU9YTSRL14B3HP85"
API_SECRET = "LygJds1CusdjC6pfN1zmPVIwUmZZerWcTAdU0Tip"
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

#file_path = "C:/Users/aarya/OneDrive/Desktop/archive/stock_market_data/nasdaq/csv/AAPL.csv"

class MLTrader(Strategy):
    def initialize(self, symbol, cash_at_risk=0.5, base_file_path="C:/Users/aarya/OneDrive/Desktop/archive/stock_market_data/nasdaq/csv/"):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None
        self.cash_at_risk = cash_at_risk
        # Construct the file path dynamically based on the symbol
        self.file_path = f"{base_file_path}{symbol}.csv"
        self.df = pd.read_csv(self.file_path)
        self.prepare_data()
        self.api = REST(base_url=BASE_URL, key_id=API_KEY, secret_key=API_SECRET)
    
    def prepare_data(self):
        # Correcting the date parsing with explicit format
        self.df['Date'] = pd.to_datetime(self.df['Date'], format='%d-%m-%Y')
        self.df.sort_values('Date', inplace=True)  # Ensure data is sorted by date
        self.df.set_index('Date', inplace=True)

    def compute_indicators(self):
        # Check the column names and adjust accordingly. Here, 'Close' is used as an example.
        macd = MACD(self.df['Close']).macd_signal()  # Adjust 'close' to 'Close' if that's the correct column name.
        rsi = RSIIndicator(self.df['Close']).rsi()  # Same adjustment here.
        bb = BollingerBands(self.df['Close'])  # And here.
        self.df['macd'] = macd
        self.df['rsi'] = rsi
        self.df['bb_high'] = bb.bollinger_hband()
        self.df['bb_low'] = bb.bollinger_lband()


        # Additional indicators can be added here as needed

    def position_sizing(self):
        cash = self.get_cash()
        last_price = self.get_last_price(self.symbol)
        quantity = round(cash * self.cash_at_risk / last_price, 0)
        return cash, last_price, quantity

    def get_dates(self):
        today = datetime.now()
        three_days_prior = today - timedelta(days=3)
        return today.strftime('%Y-%m-%d'), three_days_prior.strftime('%Y-%m-%d')

    def get_sentiment(self):
        today, three_days_prior = self.get_dates()
        news = self.api.get_news(symbol=self.symbol, start=three_days_prior, end=today)
        news = [ev.__dict__["_raw"]["headline"] for ev in news]
        probability, sentiment = estimate_sentiment(news)
        return probability, sentiment

    def on_trading_iteration(self):
        self.compute_indicators()  # Make sure to call this to update indicators
        cash, last_price, quantity = self.position_sizing()
        probability, sentiment = self.get_sentiment()

        if cash > last_price: 
            if sentiment == "positive" and probability > .90: 
                if self.last_trade == "sell": 
                    self.sell_all() 
                order = self.create_order(
                    self.symbol, 
                    quantity, 
                    "buy", 
                    type="bracket", 
                    take_profit_price=last_price*1.20, 
                    stop_loss_price=last_price*.95
                )
                self.submit_order(order) 
                self.last_trade = "buy"
            elif sentiment == "negative" and probability > .999: 
                if self.last_trade == "buy": 
                    self.sell_all() 
                order = self.create_order(
                    self.symbol, 
                    quantity, 
                    "sell", 
                    type="bracket", 
                    take_profit_price=last_price*.8, 
                    stop_loss_price=last_price*1.05
                )
                self.submit_order(order) 
                self.last_trade = "sell"

start_date = datetime(2021,1,1)
end_date = datetime(2024,2,1) 
broker = Alpaca(ALPACA_CREDS) 
strategy = MLTrader(name='mlstrat', broker=broker, 
                    parameters={"symbol":"AAPL", 
                                "cash_at_risk":.5})
strategy.backtest(
    YahooDataBacktesting, 
    start_date, 
    end_date, 
    parameters={"symbol":"AAPL", "cash_at_risk":.5}
)
trader = Trader()
trader.add_strategy(strategy)
trader.run_all()