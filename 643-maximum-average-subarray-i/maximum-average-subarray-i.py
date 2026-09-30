class Solution(object):
    def findMaxAverage(self, nums, k):
        j = 0
        sum = 0
        ans = -float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            if i-j+1 == k:
                ans = max(ans, sum)
                sum -= nums[j]
                j += 1
        return float(ans)/k
        