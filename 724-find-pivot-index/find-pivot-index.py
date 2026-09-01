class Solution(object):
    def pivotIndex(self, nums):
        
        prefix_start = []
        sum_start = 0
        
        for i in range(len(nums)):
            sum_start += nums[i]
            prefix_start.append(sum_start)

        prefix_end = [0] * len(nums)
        sum_end = 0
        
        for i in range(len(nums) - 1, -1, -1):
            sum_end += nums[i]
            prefix_end[i] = sum_end

        for i in range(len(nums)):
            
            left_sum = 0
            right_sum = 0
            
            if i > 0:
                left_sum = prefix_start[i - 1]
            
            if i < len(nums) - 1:
                right_sum = prefix_end[i + 1]
            
            if left_sum == right_sum:
                return i
        
        return -1