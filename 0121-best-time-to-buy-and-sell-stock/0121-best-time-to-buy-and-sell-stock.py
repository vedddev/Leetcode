class Solution(object):
    def maxProfit(self, prices):
        buy=float('inf')
        profit=0
        for price in prices:
            if buy>price:
                buy=price
            else:
                profit=max(profit,price-buy)
        return profit