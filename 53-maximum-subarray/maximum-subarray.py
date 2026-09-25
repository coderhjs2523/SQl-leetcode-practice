class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        ans = float('-inf')
        for ele in nums:
            sum += ele
            ans = max(ans, sum)
            if sum < 0:
                sum = 0
        return ans
        