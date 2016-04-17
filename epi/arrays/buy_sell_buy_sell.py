import sys

def buy_sell_buy_sell(arr):
    # Find the first buy sell max profit we can gain.
    min_price = sys.maxsize
    first_buy_sell = [0] * (len(arr) + 1)
    max_profit = 0
    for i, price in enumerate(arr):
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
        first_buy_sell[i+1] = max_profit
    
    print(first_buy_sell)
    
    # Now do the 2nd pass from the end to find out which one is the max.
    max_price_so_far = 0
    max_profit_so_far = 0
    profits = [0] * (len(arr) + 1)
    for i in range(len(arr) - 1, 0, -1):
        max_price_so_far = max(max_price_so_far, arr[i])
        print("i: %s, max_price_so_far: %s, price[i]: %s, first_buy_sell: %s" % (i, max_price_so_far, arr[i], first_buy_sell[i]))
        max_profit_so_far = max(max_profit_so_far, max_price_so_far - arr[i] + first_buy_sell[i])
        profits[i] = max_profit_so_far
        
    print("Profits: " + str(profits))
    print("Max Profit: " + str(max_profit_so_far))

arr = [12, 11, 13, 9, 12, 8, 14, 13, 15]

buy_sell_buy_sell(arr)