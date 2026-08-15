class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxcount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxcount = max(count, maxcount)
            else:
                count = 0
        return maxcount