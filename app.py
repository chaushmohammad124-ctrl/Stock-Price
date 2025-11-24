from flask import Flask, render_template, jsonify, request
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import random

app = Flask(__name__)

# Expanded list of popular stocks
POPULAR_STOCKS = {
    'AAPL': 'Apple Inc.', 'MSFT': 'Microsoft Corporation', 'GOOGL': 'Alphabet Inc.',
    'AMZN': 'Amazon.com Inc.', 'META': 'Meta Platforms Inc.', 'NVDA': 'NVIDIA Corporation',
    'TSLA': 'Tesla Inc.', 'JPM': 'JPMorgan Chase & Co.', 'V': 'Visa Inc.', 'MA': 'Mastercard Inc.',
    'WMT': 'Walmart Inc.', 'DIS': 'Walt Disney Company', 'NFLX': 'Netflix Inc.',
    'INTC': 'Intel Corporation', 'AMD': 'Advanced Micro Devices Inc.', 'PYPL': 'PayPal Holdings Inc.',
}

# Mock prices for demonstration when API fails
MOCK_PRICES = {
    'AAPL': 195.50, 'MSFT': 420.75, 'GOOGL': 145.30, 'AMZN': 185.90,
    'TSLA': 185.25, 'META': 510.40, 'NVDA': 880.65, 'JPM': 200.10,
    'V': 295.20, 'WMT': 175.60, 'DIS': 115.80, 'NFLX': 680.45,
}

def generate_mock_history(base_price, count):
    """Generate mock stock history"""
    history = []
    price = base_price
    for i in range(count):
        price = price * (1 + random.uniform(-0.015, 0.015))
        history.append({
            'date': (datetime.now() - timedelta(hours=count-i)).strftime('%Y-%m-%d %H:%M:%S'),
            'price': round(price, 2),
            'volume': random.randint(1000000, 10000000)
        })
    return history

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stock/<symbol>')
def get_stock_data(symbol):
    symbol = symbol.upper()
    print(f"Fetching {symbol}...")
    
    # Use mock data (Yahoo Finance is being rate-limited)
    base_price = MOCK_PRICES.get(symbol, 150.00)
    current_price = round(base_price * random.uniform(0.98, 1.02), 2)
    previous_close = base_price
    change = round(current_price - previous_close, 2)
    change_percent = round((change / previous_close) * 100, 2)
    
    return jsonify({
        'symbol': symbol,
        'name': POPULAR_STOCKS.get(symbol, f'{symbol} Corporation'),
        'price': current_price,
        'change': change,
        'changePercent': change_percent,
        'open': round(base_price * 1.005, 2),
        'high': round(current_price * 1.015, 2),
        'low': round(current_price * 0.985, 2),
        'volume': random.randint(50000000, 150000000),
        'marketCap': random.randint(500000000000, 3000000000000),
        'pe': round(random.uniform(15, 35), 2),
        'fiftyTwoWeekHigh': round(current_price * 1.25, 2),
        'fiftyTwoWeekLow': round(current_price * 0.75, 2),
        'history': {
            '1d': generate_mock_history(current_price, 78),
            '1w': generate_mock_history(current_price, 65),
            '1m': generate_mock_history(current_price, 21),
            '3m': generate_mock_history(current_price, 63),
            '1y': generate_mock_history(current_price, 252)
        }
    })

@app.route('/api/search/<query>')
def search_stocks(query):
    query = query.upper()
    results = [{'symbol': k, 'name': v} for k, v in POPULAR_STOCKS.items() if query in k or query in v.upper()]
    return jsonify(results[:10])

@app.route('/api/news/<symbol>')
def get_stock_news(symbol):
    mock_news = [
        {'title': f'{symbol} Stock Analysis: Market Updates', 'publisher': 'Financial Times', 'link': '#',
         'publishedAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
        {'title': f'{symbol} Quarterly Earnings Beat Expectations', 'publisher': 'Bloomberg', 'link': '#',
         'publishedAt': (datetime.now() - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')},
        {'title': f'Analysts Upgrade {symbol} to Buy', 'publisher': 'CNBC', 'link': '#',
         'publishedAt': (datetime.now() - timedelta(hours=6)).strftime('%Y-%m-%d %H:%M:%S')}
    ]
    return jsonify(mock_news)

@app.route('/api/indicators/<symbol>')
def get_technical_indicators(symbol):
    base_price = MOCK_PRICES.get(symbol, 150)
    return jsonify({
        'rsi': round(random.uniform(30, 70), 2),
        'macd': round(random.uniform(-5, 5), 2),
        'macd_signal': round(random.uniform(-5, 5), 2),
        'ma_20': round(base_price * random.uniform(0.95, 1.05), 2),
        'ma_50': round(base_price * random.uniform(0.90, 1.10), 2)
    })

@app.route('/api/compare')
def compare_stocks():
    symbols = request.args.get('symbols', '').split(',')
    if not symbols or len(symbols) < 2:
        return jsonify({'error': 'Please provide at least 2 symbols'}), 400
    
    comparison_data = []
    for symbol in symbols[:4]:
        symbol = symbol.strip().upper()
        base_price = MOCK_PRICES.get(symbol, 100)
        current_price = round(base_price * random.uniform(0.98, 1.02), 2)
        comparison_data.append({
            'symbol': symbol,
            'name': POPULAR_STOCKS.get(symbol, f'{symbol} Corporation'),
            'price': current_price,
            'change': round(current_price - base_price, 2),
            'changePercent': round((current_price - base_price) / base_price * 100, 2),
            'marketCap': random.randint(500000000000, 3000000000000),
            'pe': round(random.uniform(15, 35), 2),
            'volume': random.randint(50000000, 150000000)
        })
    return jsonify(comparison_data)

if __name__ == '__main__':
    print("=" * 60)
    print("Stock Market Dashboard Starting...")
    print("Server: http://localhost:5007")
    print("=" * 60)
    app.run(debug=True, port=5007, use_reloader=False)
