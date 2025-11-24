# 📈 Stock Market Dashboard

A beautiful, feature-rich real-time stock market dashboard built with Flask and powered by Yahoo Finance API. Track stocks, view charts, manage watchlists, compare stocks, and stay updated with the latest market news.

![Stock Market Dashboard](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### Core Features
- **Real-time Stock Data**: Get live stock prices, changes, and market data
- **Interactive Charts**: View stock performance across multiple timeframes (1D, 1W, 1M, 3M, 1Y)
- **Company Logos**: Display real company logos for better visual identification
- **Search Functionality**: Search any stock by symbol or company name
- **Quick Picks**: Fast access to popular stocks (AAPL, MSFT, GOOGL, TSLA, etc.)

### Advanced Features
- **📋 Watchlist**: Save and track your favorite stocks with persistent storage
- **📊 Stock Comparison**: Compare multiple stocks side-by-side
- **📰 Live News Feed**: Get the latest news for each stock
- **📈 Technical Indicators**: RSI, MACD, and Moving Averages
- **💼 Portfolio Tracker**: Virtual portfolio with buy/sell tracking
- **🔔 Price Alerts**: Set custom price alerts for stocks
- **📥 Export Data**: Download stock data as CSV

### UI/UX Features
- **Glassmorphic Design**: Modern, premium dark-themed interface
- **Animated Background**: Floating particle effects
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile
- **Smooth Animations**: Engaging micro-interactions and transitions
- **Color-coded Charts**: Green for gains, red for losses

## 🚀 Demo

![Stock Dashboard Screenshot](https://raw.githubusercontent.com/yourusername/stock-market-dashboard/main/screenshots/dashboard_main.png)

*Beautiful glassmorphic design with real company logos, real-time data, and interactive charts*

**Key UI Features Visible:**
- Company logo integration (Clearbit API)
- Real-time stock price with color-coded changes
- Interactive price chart with multiple timeframes
- Stock information cards with glassmorphism effects
- Animated background particles
- Watchlist sidebar for saving favorite stocks
- Technical indicators (RSI, MACD, Moving Averages)
- Live news feed

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Data Source**: yfinance (Yahoo Finance API)
- **Charts**: Chart.js
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data Processing**: Pandas
- **Icons**: Clearbit Logo API

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for real-time stock data)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chaushmohammad124-ctrl/Stock-Price.git
   cd stock-market-dashboard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   Navigate to: http://localhost:5007
   ```

## 📖 Usage

### Search for Stocks
- Type any stock symbol (e.g., AAPL, TSLA) or company name in the search box
- Select from the dropdown suggestions or press Enter to search

### View Stock Details
- Click on any stock to view detailed information
- See current price, day range, volume, and market cap
- View interactive price charts with multiple timeframes

### Manage Watchlist
- Click the "Add to Watchlist" button to save stocks
- Access your watchlist from the sidebar
- Remove stocks by clicking the remove icon

### Compare Stocks
- Select multiple stocks to compare side-by-side
- View comparative charts and metrics

### Track Portfolio
- Add virtual buy/sell transactions
- Track your portfolio performance
- View profit/loss calculations

## 🏗️ Project Structure

```
stock-market-dashboard/
│
├── app.py                 # Flask application & API routes
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore rules
│
└── templates/
    └── index.html        # Main dashboard page
```

## 🔌 API Endpoints

### Get Stock Data
```
GET /api/stock/<symbol>
```
Returns comprehensive stock data including price, history, and market info.

### Search Stocks
```
GET /api/search/<query>
```
Search for stocks by symbol or company name.

### Get Stock News
```
GET /api/news/<symbol>
```
Fetch latest news articles for a specific stock.

### Technical Indicators
```
GET /api/indicators/<symbol>
```
Get RSI, MACD, and Moving Average data.

## 🎨 Customization

### Change Default Stock
Edit `index.html` at line 716:
```javascript
loadStock('AAPL');  // Change 'AAPL' to your preferred stock
```

### Modify Quick Picks
Edit `index.html` at lines 426-431 to change the quick pick stocks.

### Adjust Port Number
Edit `app.py` at line 88:
```python
app.run(debug=True, port=5007)  # Change port number
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Stock data provided by [Yahoo Finance](https://finance.yahoo.com/) via yfinance
- Company logos from [Clearbit Logo API](https://clearbit.com/logo)
- Chart library: [Chart.js](https://www.chartjs.org/)
- Icons and emojis for enhanced UI

## 📧 Contact

Your Name - [@chaushmohammad](https://twitter.com/chaushmohammad)


## ⚠️ Disclaimer

This dashboard is for educational and informational purposes only. It should not be considered financial advice. Always do your own research and consult with a qualified financial advisor before making investment decisions.

---

**Made with ❤️ and Python**

