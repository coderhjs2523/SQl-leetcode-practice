class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        count = 0
        ans = 0

        for ele in nums:

            if ele == 1:
                count += 1
            else:
                ans = max(ans, count)
                count = 0
        
        return max(ans, count)
        