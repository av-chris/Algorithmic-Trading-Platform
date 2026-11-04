import vectorbt as vbt


price = vbt.YFData.download('NVDA', start='2020-01-01', end='2026-01-01').get('Close')




fastMovingAverege = vbt.MA.run(price, window=10)

slowMovingAverege = vbt.MA.run(price, window=50)

entries = fastMovingAverege.ma_crossed_above(slowMovingAverege)

exits = fastMovingAverege.ma_crossed_below(slowMovingAverege)

rsi = vbt.RSI.run(price, window=14)      # RSI

portfolio = vbt.Portfolio.from_signals(

        price, entries, exits,

        init_cash=10000,
        fees=0.001,
        freq='1D'
)

print(portfolio.stats())
print(portfolio.total_return())
print(portfolio.sharpe_ratio())
print(portfolio.max_drawdown())
portfolio.plot().show()
