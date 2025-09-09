# main.py
from bot import BasicBot
from config import API_KEY, API_SECRET, TESTNET
from utils import get_valid_symbol, get_valid_quantity, get_valid_price

def main():
    bot = BasicBot(API_KEY, API_SECRET, TESTNET)
    print("\n=== Welcome to Advanced Binance Testnet Bot ===\n")

    while True:
        print("\nMenu:")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Place Stop-Limit Order")
        print("4. Place OCO Order")
        print("5. Check Account Balance")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "0":
            print("Exiting...")
            break

        symbol = get_valid_symbol(bot)
        side = input("Side (BUY/SELL): ").upper()
        quantity = get_valid_quantity(bot, symbol)

        if choice == "1":
            bot.place_market_order(symbol, side, quantity)

        elif choice == "2":
            price = get_valid_price(bot, symbol, "Limit Price: ")
            bot.place_limit_order(symbol, side, quantity, price)

        elif choice == "3":
            stop_price = get_valid_price(bot, symbol, "Stop Price: ")
            limit_price = get_valid_price(bot, symbol, "Limit Price: ")
            bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)

        elif choice == "4":
            price = get_valid_price(bot, symbol, "Limit Price: ")
            stop_price = get_valid_price(bot, symbol, "Stop Price: ")
            bot.place_oco_order(symbol, side, quantity, price, stop_price)

        elif choice == "5":
            bot.check_balance()

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
