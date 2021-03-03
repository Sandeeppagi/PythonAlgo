def buy_and_sell_stock_once(price):
    """
    Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be
    made from buying on one day and selling on another.

    In an array of prices, each index represents a day, and the value on that index represents the price of the
    stocks on that day.

    Here is the way to calculate the profit:

    Profit = Selling Price - Buying Price

    Note that you need to buy the stocks before you sell them so the day (index) indicating the buying price should
    be before the day (index) indicating the selling price. :param prices:

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    i = 0
    max_profit = 0
    while i < len(price) - 1:
        j = i + 1
        while j < len(price):
            profit = price[j] - price[i]
            if max_profit < profit:
                max_profit = profit
            j += 1
        i += 1
    print(max_profit)


def buy_and_sell_stock_once_v2(price):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param price:
    :return:
    """
    max_profit = 0.0
    min_price = float('inf')
    for today_price in price:
        min_price = min(today_price, min_price)
        profit = today_price - min_price
        max_profit = max(profit, max_profit)
    print(max_profit)


price = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
buy_and_sell_stock_once(price)
buy_and_sell_stock_once_v2(price)
