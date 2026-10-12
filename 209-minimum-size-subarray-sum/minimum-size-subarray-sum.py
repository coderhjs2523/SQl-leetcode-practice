class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        j = 0
        sum = 0
        ans = float('inf')

        for i in range(len(nums)):
            sum += nums[i] 


            while sum >= target:
                sum -= nums[j]
                ans = min(ans, i-j+1)
                j += 1

        if ans == float('inf'):
            return 0
        return ans