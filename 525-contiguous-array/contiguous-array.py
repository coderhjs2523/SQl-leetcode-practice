class Solution(object):
    def findMaxLength(self, nums):
        map = {}
        map[0] = -1
        maxlength = 0
        current_sum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                current_sum += -1
            else:
                current_sum += 1

            if current_sum in map:
                maxlength = max(maxlength, i-map[current_sum])
            else:
                map[current_sum] = i
        return maxlength