class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        j = 0
        sum = 0
        ans = len(nums) + 1

        for i in range(len(nums)):
            sum += nums[i] 

            while sum >= target:
                sum -= nums[j]
                ans = min(ans, i-j+1)
                j += 1

        return 0 if ans > len(nums) else ans