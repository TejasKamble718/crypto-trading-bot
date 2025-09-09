# bot.py
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from logger import logger

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        logger.info("Initialized Binance Testnet Client")

    def get_current_price(self, symbol):
        try:
            ticker = self.client.futures_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])
            logger.info(f"Current price of {symbol}: {price}")
            return price
        except Exception as e:
            logger.error(f"Failed to fetch current price for {symbol}: {e}")
            return None

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
            logger.info(f"Market Order Response: {order}")
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"Market order failed: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logger.info(f"Limit Order Response: {order}")
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"Limit order failed: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="STOP_MARKET",
                stopPrice=stop_price,
                quantity=quantity
            )
            logger.info(f"Stop-Limit Order Response: {order}")
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"Stop-Limit order failed: {e}")
            return None

    def place_oco_order(self, symbol, side, quantity, price, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="OCO",
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )
            logger.info(f"OCO Order Response: {order}")
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"OCO order failed: {e}")
            return None

    def check_balance(self):
        try:
            balances = self.client.futures_account_balance()
            logger.info("Account Balances:")
            for b in balances:
                if float(b['balance']) > 0:
                    logger.info(f"{b['asset']}: {b['balance']}")
            return balances
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"Failed to fetch balances: {e}")
            return None
