class Solution(object):
    def findMaxAverage(self, nums, k):
        window = 0
        i = 0

        while i < k:
            window += nums[i]
            i += 1

        start = 0
        end = k
        maxsum = window

        while end < len(nums):
            window -= nums[start]
            start += 1

            window += nums[end]
            end += 1

            maxsum = max(maxsum, window)

        return float(maxsum) / k