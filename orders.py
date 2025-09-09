from binance.client import Client
from logger import log_info, log_error
from config import API_KEY, API_SECRET, BASE_URL
import time

class TradingBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.FUTURES_URL = BASE_URL

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:
        for attempt in range(3):  # Retry logic
            try:
                log_info(f"Placing {order_type} order | Symbol: {symbol}, Side: {side}, Qty: {quantity}, Price: {price}")
                
                if order_type == 'MARKET':
                    order = self.client.futures_create_order(
                        symbol=symbol,
                        side=side,
                        type='MARKET',
                        quantity=quantity
                    )
                elif order_type == 'LIMIT':
                    order = self.client.futures_create_order(
                        symbol=symbol,
                        side=side,
                        type='LIMIT',
                        timeInForce='GTC',
                        quantity=quantity,
                        price=price
                    )
                else:
                    raise ValueError("Unsupported order type")

                log_info(f"Order response: {order}")
                return order

            except Exception as e:
                log_error(f"Attempt {attempt+1} failed: {e}")
                time.sleep(2 ** attempt)
        return None

    def place_grid_orders(self, symbol: str, side: str, quantity: float, start_price: float, end_price: float, steps: int):
        price_step = round((end_price - start_price) / steps, 2)
        for i in range(steps):
            price = round(start_price + i * price_step, 2)
            print(f"Placing grid order {i+1}/{steps} at price {price}")
            self.place_order(symbol, side, 'LIMIT', quantity, price)
