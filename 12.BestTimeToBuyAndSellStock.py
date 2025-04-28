from typing import List

# 27ms
def maxProfit_me(prices: List[int]) -> int:
    buy,sell = 10001,0
    for i in prices:
        if i<buy:buy = i
        elif sell<i-buy:sell = i-buy
    
    return sell

print(maxProfit_me([7,6,4,3,1]))

# 82ms
def maxProfit(prices: List[int]) -> int:
    buy=prices[0]
    profit=0
    for p in prices[1:]:
        if buy>p:
            buy=p
        profit=max(profit,p-buy)
    return profit

# 142ms
def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit