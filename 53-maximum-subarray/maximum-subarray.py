class Solution(object):
    def maxSubArray(self, nums):
        currentSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            currentSum += nums[i]
            maxSum = max(maxSum, currentSum)
            if currentSum < 0:
                currentSum = 0
        return maxSum 
        
        