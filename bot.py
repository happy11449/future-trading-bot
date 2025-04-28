# Connect to Binance Futures Testnet using the provided API Key and Secret Key
from binance.client import Client
import sys  # to allow program exit on failure

# Binance Futures Testnet API credentials (replace with your own if needed)
api_key = "96fa5c2fb6f5931c253bf0605417b72befbd6b5bd298284433c8dedcadd149e"
api_secret = "601a2bd0c8cf65fde57027a6a6e00f5814938e200efff03c1a62b5eb10695a1"

# Initialize the Binance Client for Futures
client = Client(api_key, api_secret)
# Set the base URL to Binance Futures Testnet 
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# Test the connection by fetching account balance or system status
try:
    # Attempt to retrieve the futures account balance (requires valid API keys)
    account_balance = client.futures_account_balance()
    # If no exception is raised up to this point, the connection was successful
    print("Connection successful!")
except Exception as e:
    # If an error occurs (e.g., invalid key, network issue), output the error message
    print(f"Connection failed: {e}")
    sys.exit(1)  # Exit the program if connection fails (optional)

# ... (Continue with the rest of the trading bot logic below)

