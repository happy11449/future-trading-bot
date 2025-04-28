import ccxt

# Your Binance Testnet API keys (from your screenshot)
api_key = '96fa5c2fb8f5931c253bf0605417b72befbd6b5bd298284433c86dacddd149e'
api_secret = '601a2bd0c8cf65fde57027a4a6e00f58149308200efff03c1a62b5eb10695a1'

# Connect to Binance Futures Testnet
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
    'options': {
        'defaultType': 'future'
    }
})

exchange.set_sandbox_mode(True)  # Activate testnet mode

def test_connection():
    try:
        balance = exchange.fetch_balance()
        print("Bot Connected Successfully!")
        print("Your Balance Snapshot:")
        print(balance)
    except Exception as e:
        print("Error connecting to Binance Futures:", str(e))

if __name__ == "__main__":
    test_connection()


