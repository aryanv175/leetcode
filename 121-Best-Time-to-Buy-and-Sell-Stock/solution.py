# 121-Best-Time-to-Buy-and-Sell-Stock
""" Logic: The logic for this problem is rather simple,
           all you need is two pointers one for the buy 
           price and one for the sell price. if the buy
           price is more than the sell price than both the
           pointers go forward. But if the sell price is 
           higher than buy price then we keep iterating 
           through the list of prices until we find the
           maximum proft (max value of sell price - buy price)."""

def maxProfit(p: List[int]) -> int:
    profit = 0
    buy = 0
    sell = 1
    while sell < len(p):
        if p[buy] < p[sell]:
            profit = max(profit, p[sell] - p[buy])
        else:
            buy = sell 
        sell += 1
    return profit
