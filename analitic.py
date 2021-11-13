from pytickersymbols import PyTickerSymbols
import investpy
import numpy as np
from datetime import date
import time


class ASD:
    def anal(a):
        stock_data = PyTickerSymbols()
        uk_stocks = stock_data.get_all_stocks()
        sign = a
        ret = ''
        country = ''
        for i in uk_stocks:
            try:
                if sign in i['symbol']:
                    country = i['country']
                    name = i['name']
            except:
                print(1)
        if country == 'Russian Federation':
            country = 'Russia'

        symbol = a
        current_date = str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year)
        a = date.today().month
        if a == 1:
            from_date = str(date.today().day) + '/' + str(12) + '/' + str(date.today().year - 1)
        else:
            from_date = str(date.today().day) + '/' + str(date.today().month - 1) + '/' + str(date.today().year)
        df = investpy.get_stock_historical_data(stock=str(symbol), country=str(country), from_date=from_date,
                                                to_date=current_date)

        technical_indicators = investpy.technical.technical_indicators(symbol, str(country), 'stock', interval='daily')
        country = str(country)

        tech_sell = len(technical_indicators[technical_indicators['signal'] == 'sell'])
        tech_buy = len(technical_indicators[technical_indicators['signal'] == 'buy'])

        moving_averages = investpy.technical.moving_averages(symbol, country, 'stock', interval='daily')
        moving_sma_sell = len(moving_averages[moving_averages['sma_signal'] == 'sell'])
        moving_sma_buy = len(moving_averages[moving_averages['sma_signal'] == 'buy'])

        moving_ema_sell = len(moving_averages[moving_averages['ema_signal'] == 'sell'])
        moving_ema_buy = len(moving_averages[moving_averages['ema_signal'] == 'buy'])
        # if tech_buy < 9 or tech_sell > 2 or moving_sma_buy < 5 or moving_ema_buy < 5:
        # continue
        sma_20 = moving_averages['sma_signal'][2]
        sma_100 = moving_averages['sma_signal'][4]
        ema_20 = moving_averages['ema_signal'][2]
        ema_100 = moving_averages['ema_signal'][4]
        print('STOCK =', symbol)
        print('Tech sell indicators: to buy =', tech_buy, 'of 12; ', 'to sell =', tech_sell, 'of 12')
        print('SMA moving averages: to buy =', moving_sma_buy, 'of 6; ', 'to sell =', moving_sma_sell, 'of 6')
        print('EMA moving averages: to buy =', moving_ema_buy, 'of 6; ', 'to sell =', moving_ema_sell, 'of 6')
        print('SMA_20 =', sma_20, ';', 'SMA_100 =', sma_100, ';', 'EMA_20 =', ema_20, ';', 'EMA_100 =', ema_100)
        print('Prices Last Five days of ' + symbol + ' =', np.array(df['Close'][-5:][0]), ';',
              np.array(df['Close'][-5:][1]),
              ';', np.array(df['Close'][-5:][2]), ';', np.array(df['Close'][-5:][3]), ';',
              np.array(df['Close'][-5:][4]))

        counter = 0
        if (sma_20 == 'buy'):
            counter = counter + 1
        else:
            counter = counter - 1
        if (sma_100 == 'buy'):
            counter = counter + 1
        else:
            counter = counter - 1
        if (ema_20 == 'buy'):
            counter = counter + 1
        else:
            counter = counter - 1
        if (ema_100 == 'buy'):
            counter = counter + 1
        else:
            counter = counter - 1

        if (counter == 4):
            ret = 'АКТИВНО ПОКУПАТЬ'
        if (counter == -4):
            ret = "АКТИВНО ПРОДОВАТЬ"
        if (counter == -3 or counter == -2):
            ret = "ПРОДОВАТЬ"
        if (counter == 3 or counter == 2):
            ret = "ПОКУПАТЬ"
        if (counter == 0 or counter == 1 or counter == -1):
            ret = "БЫТЬ НЕЙТРАЛЬНЫМ"

        return tech_buy, tech_sell, moving_sma_buy, moving_sma_sell, moving_ema_buy, moving_ema_sell, sma_20, sma_100, ema_20, ema_100, np.array(
            df['Close'][-15:][0]), np.array(df['Close'][-15:][1]), np.array(df['Close'][-15:][2]), np.array(
            df['Close'][-15:][3]), np.array(df['Close'][-15:][4]), np.array(df['Close'][-15:][5]), np.array(
            df['Close'][-15:][6]), np.array(df['Close'][-15:][7]), np.array(df['Close'][-15:][8]), np.array(
            df['Close'][-15:][9]), np.array(df['Close'][-15:][10]), np.array(df['Close'][-15:][11]), np.array(
            df['Close'][-15:][12]), np.array(df['Close'][-15:][13]), np.array(df['Close'][-15:][14]), ret
