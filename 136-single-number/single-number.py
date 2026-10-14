class Solution(object):
    def singleNumber(self, nums):
        
        ans = nums[0]

        for i in range(1,len(nums)):
            ans ^= nums[i]
        
        return ans