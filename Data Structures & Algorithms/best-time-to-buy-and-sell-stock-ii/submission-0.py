class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            profit = price - min_price
            if profit > 0:
             max_profit += profit
            min_price = price
        return max_profit
        