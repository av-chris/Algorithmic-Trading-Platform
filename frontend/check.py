from Quant.backtest import moving_average_strategy, print_portfolio

stock = input("Input Stock Name: ")
shortWindow = int(input("Input Short Window: "))
longWindow = int(input("Input Long Window: "))
startDay = input("Input Start Day: ")
endDay = input("Input End Day: ")


portfolio = moving_average_strategy(stock, shortWindow, longWindow, startDay, endDay)

print_portfolio(portfolio)
