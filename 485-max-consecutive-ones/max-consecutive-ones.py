class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ans = 0
        count = 0
        for ele in nums:
            if ele == 1:
                count += 1
            else:
                ans = max(ans, count)
                count = 0
        ans = max(ans, count)
        return ans
        