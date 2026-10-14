class Solution(object):
    def maxProfit(self, prices):
        
        buy_price = prices[0]
        ans = 0
        profit = 0

        for i in range(1,len(prices)):

            if prices[i] - buy_price > profit:
                profit = prices[i] - buy_price
                ans = max(ans, profit)

            buy_price = min(buy_price, prices[i])

        return ans