class Solution(object):
    def maxProfit(self, prices):
        
        buy_price = prices[0]
        ans = 0
        profit = 0

        for i in range(1,len(prices)):

            if prices[i] - buy_price > profit:
                ans = max(ans, prices[i] - buy_price)

            buy_price = min(buy_price, prices[i])

        return ans