class Solution(object):
    def maxProfit(self, prices):
        buy_day = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > buy_day:
                max_profit = max(max_profit, prices[i]-buy_day)
            buy_day = min(buy_day, prices[i])
        return max_profit