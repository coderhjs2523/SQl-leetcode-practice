class Solution(object):
    def minStartValue(self, nums):
        
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]

        ans = nums[0]

        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            ans = min(ans, prefix_sum[i])

        if ans<=0:
            return abs(ans)+1
        return 1