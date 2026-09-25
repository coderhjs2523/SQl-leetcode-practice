class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        Natural_sum = n*(n+1)/2
        sum = 0
        for ele in nums:
            sum += ele
        return Natural_sum - sum