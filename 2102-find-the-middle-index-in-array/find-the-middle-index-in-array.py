class Solution(object):
    def findMiddleIndex(self, nums):
        
        n = len(nums)
        prefix = 0

        for i in range(n):
            prefix += nums[i]

        left_sum = 0
        
        for i in range(n):
            right_sum = prefix - nums[i] - left_sum

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1