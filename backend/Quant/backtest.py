import vectorbt as vbt

#Moving Avarege 

def moving_average_strategy(stock, shortWindow, longWindow,startDay,endDay):
    price = vbt.YFData.download(stock, start = startDay, end =endDay).get('Close')

    fastMA = vbt.MA.run(price, window = shortWindow)
    slowMA = vbt.MA.run(price, window = longWindow)

    enteries = fastMA.ma_crossed_above(slowMA)
    exits = fastMA.ma_crossed_below(slowMA)

    portfolio = vbt.Portfolio.from_signals(price, enteries, exits, init_cash= 10000, fees=0.001, freq= '1d')

    return portfolio

def print_portfolio(portfolio):
    print(portfolio.stats())
    print(portfolio.total_return())
    print(portfolio.sharpe_ratio())
    print(portfolio.max_drawdown())
    portfolio.plot().show()