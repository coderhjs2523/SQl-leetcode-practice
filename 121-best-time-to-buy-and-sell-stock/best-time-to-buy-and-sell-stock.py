class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        buyDay = prices[0]

        for i in range(1,len(prices)):
            if buyDay < prices[i]:
                maxprofit = max(maxprofit, prices[i]-buyDay)
            buyDay = min(buyDay, prices[i])
        return maxprofit
        