# Trading Bot (Binance Futures Testnet)

## Overview

This project is a simplified Python-based trading bot designed to place Market and Limit orders on Binance Futures.

It provides a clean and modular structure with:

* CLI-based input
* Logging
* Error handling
* Input validation

---

## Features

* Place MARKET and LIMIT orders
* Supports both BUY and SELL
* Command-line interface using argparse
* Structured code (client, orders, validators)
* Logging of requests, responses, and errors
* Input validation for safer execution

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client setup
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
├── .env                   # API keys (not shared)
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/mudgalshriya2004-eng/trading-bot.git
cd trading_bot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add API credentials

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## How to Run

### Market Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
```

---

## Sample Output

```
Order Summary
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.01}

Order Success
Order ID: TEST123456
Status: FILLED
Executed Qty: 0.01
Avg Price: MARKET
```

---

## Logging

All API activity and errors are logged in:

```
bot.log
```

---

## Note

Due to regional restrictions and verification requirements on Binance Testnet, a mock order execution layer has been implemented.

The application is structured to support real API integration, and switching to live/testnet trading requires only updating the client configuration.

---

## Assumptions

* User provides valid CLI inputs
* Internet connection is stable
* API keys are securely stored in `.env`

---

## Future Improvements

* Add Stop-Limit or OCO orders
* Improve CLI experience with interactive prompts
* Add a lightweight UI
* Implement risk management features

---

## Author

Shriya Mudgal
