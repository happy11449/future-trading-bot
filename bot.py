import ccxt
import time
import pandas as pd

# Your Binance Futures Testnet API credentials
api_key = '96fa5c2fbb6f5931c253bf0605417b72befdb6d5bd298284433c86dacddd149e'
secret_key = '601a2bd0c8cf56fde57027a46ae60f85189320e200efff03c1a62b5eb10695a1'

# Connect to Binance Futures Testnet
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': secret_key,
    'options': {
        'defaultType': 'future',  # Important for Futures Trading
    },
    'urls': {
        'api': {
            'public': 'https://testnet.binancefuture.com/fapi/v1',
            'private': 'https://testnet.binancefuture.com/fapi/v1',
        }
    }
})

def fetch_symbols():
    try:
        markets = exchange.load_markets()
        symbols = []
        for symbol in markets:
            if '/USDT' in symbol:
                symbols.append(symbol)
        return symbols
    except Exception as e:
        print(f"Error fetching symbols: {e}")
        return []

def fetch_ohlcv(symbol, timeframe='1m', limit=20):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        return df
    except Exception as e:
        print(f"Error fetching OHLCV for {symbol}: {e}")
        return None

def analyze(df):
    if df is None or df.empty:
        return 'WAIT'
    
    last_candle = df.iloc[-1]
    prev_candle = df.iloc[-2]
    
    if last_candle['close'] > prev_candle['close'] and last_candle['volume'] > prev_candle['volume']:
        return 'BUY'
    elif last_candle['close'] < prev_candle['close'] and last_candle['volume'] > prev_candle['volume']:
        return 'SELL'
    else:
        return 'WAIT'

def main():
    print("✅ Sneak Peek Bot Started on Binance Futures Testnet!\n")
    symbols = fetch_symbols()
    if not symbols:
        print("❌ No tradable Futures pairs found!")
        return
    
    print(f"✅ Found {len(symbols)} Futures pairs to scan.\n")
    
    while True:
        for symbol in symbols:
            df = fetch_ohlcv(symbol)
            signal = analyze(df)
            print(f"{symbol} ➔ Signal: {signal}")
            time.sleep(0.5)

        print("\n🔄 Scanning again in 60 seconds...\n")
        time.sleep(60)

if __name__ == "__main__":
    main()
