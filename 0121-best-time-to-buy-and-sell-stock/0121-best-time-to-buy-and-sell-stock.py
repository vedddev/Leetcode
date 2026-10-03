class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        profit=0
        for price in prices:
            if buy>price:
                buy=price
            else:
                profit=max(profit,price-buy)
        return profit