# Binance Futures Testnet Trading Bot

A professional **Python trading bot** for Binance Futures Testnet (USDT-M) designed for learning and mock trading.

---

## Features
- Place **Market Orders**, **Limit Orders**, **Stop-Limit Orders**, and **OCO Orders**  
- **Check account balance** on Binance Futures Testnet  
- **Live market price fetching** before placing orders  
- Menu-driven **CLI interface** with input validation  
- **Logging** of all orders and errors (console + file)  
- Modular, reusable, and interview-ready code

---

## Project Structure
crypto-trading-bot/
├─ bot.py # Main bot class
├─ utils.py # Input validation
├─ logger.py # Logging setup
├─ config.py # API keys & settings
├─ main.py # CLI interface
├─ requirements.txt
└─ README.md


---

## Setup Instructions

1. **Clone the repository**
```bash
git clone <repo-url>
cd crypto-trading-bot

2. **Install dependencies**
pip install -r requirements.txt


3. **Create a Binance Testnet account**
Visit Binance Futures Testnet
Sign up or log in

4. **Generate API Key & Secret**
Go to API Management → Create a new API Key
Copy the API Key and API Secret


5. **Insert API keys into config.py**
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"


6. **Run the bot**
python main.py

**Usage**
Follow the menu to place orders:
Market Order
Limit Order
Stop-Limit Order
OCO Order
Check Account Balance
The bot will display current market price before placing limit or stop orders.
Logs are stored in trading_bot.log for auditing.