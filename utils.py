# utils.py
from logger import logger

def get_valid_symbol(bot):
    info = bot.client.futures_exchange_info()
    symbols = [s['symbol'] for s in info['symbols']]
    while True:
        symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
        if symbol in symbols:
            return symbol
        else:
            print("Invalid symbol. Try again.")

def get_valid_quantity(bot, symbol):
    while True:
        try:
            quantity = float(input("Quantity: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be positive.")
        except ValueError:
            print("Invalid input, enter a number.")

def get_valid_price(bot=None, symbol=None, prompt="Price: "):
    while True:
        try:
            if bot and symbol:
                current_price = bot.get_current_price(symbol)
                print(f"Current market price of {symbol}: {current_price}")
            price = float(input(prompt))
            if price > 0:
                return price
            else:
                print("Price must be positive.")
        except ValueError:
            print("Invalid input, enter a number.")
