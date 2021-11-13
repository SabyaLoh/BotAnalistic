from pytickersymbols import PyTickerSymbols

stock_data = PyTickerSymbols()
uk_stocks = stock_data.get_all_stocks()
sign = input()

for i in uk_stocks:
    if sign in i['symbol']:
        print(i)
