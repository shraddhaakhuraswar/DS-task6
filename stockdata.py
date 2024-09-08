import requests as rq


cUrl = 'https://api.coinbase.com/v2/exchange-rates'


stockdata = [
    {'stockname': 'AAPL', 'price': 180, 'currency': 'USD'},
    {'stockname': 'TSLA', 'price': 700, 'currency': 'USD'},
    {'stockname': 'BMW', 'price': 85, 'currency': 'EUR'},
    {'stockname': 'HSBC', 'price': 400, 'currency': 'GBP'},
    {'stockname': 'SONY', 'price': 12000, 'currency': 'JPY'},
    {'stockname': 'VOD', 'price': 130, 'currency': 'GBP'},
    {'stockname': 'SAP', 'price': 110, 'currency': 'EUR'},
    {'stockname': 'HDFC', 'price': 1200, 'currency': 'INR'},
    {'stockname': 'NESTLE', 'price': 2100, 'currency': 'CHF'},
    {'stockname': 'INFY', 'price': 1500, 'currency': 'INR'},
    {'stockname': 'MSFT', 'price': 305, 'currency': 'USD'},
    {'stockname': 'RELI', 'price': 2400, 'currency': 'INR'},
    {'stockname': 'WIPRO', 'price': 400, 'currency': 'INR'},
    {'stockname': 'ADANI', 'price': 960, 'currency': 'INR'},
    {'stockname': 'BABA', 'price': 140, 'currency': 'USD'},
    {'stockname': 'ORCL', 'price': 90, 'currency': 'USD'},
    {'stockname': 'TSM', 'price': 110, 'currency': 'USD'},
    {'stockname': 'AIR', 'price': 130, 'currency': 'EUR'},
    {'stockname': 'PFE', 'price': 45, 'currency': 'USD'},
    {'stockname': 'COCA-COLA', 'price': 60, 'currency': 'USD'},
]


def getcurrencyrates(price, currency):
    try:
        cresp = rq.get(url=cUrl)
        
        if cresp.status_code == 200:
            rates = cresp.json()['data']['rates']

            if currency == 'INR':
                USDrate = float(rates['USD'])
                new_price = price * USDrate
                print(f'{price} INR = {new_price:.2f} USD')
                return new_price
            else:
                INRrate = float(rates['INR'])
                currency_rate = float(rates[currency])
                new_price = price / currency_rate * INRrate
                print(f'{price} {currency} = {new_price:.2f} INR')
                return new_price
        else:
            print(f"Failed to fetch currency rates. Status code: {cresp.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

newstocklist = []
for stock in stockdata:
    currency = stock['currency']
    price = stock['price']
    
    print(f"Converting {stock['stockname']} price {price} {currency}...")

    new_currency_rate = getcurrencyrates(price, currency)
    if new_currency_rate:
        stock['exchangerate'] = new_currency_rate
        newstocklist.append(stock)

print("\nUpdated stock data with converted prices:")
for stock in newstocklist:
    print(stock)
