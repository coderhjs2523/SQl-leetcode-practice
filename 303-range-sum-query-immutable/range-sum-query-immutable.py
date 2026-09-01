class NumArray(object):

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0

        while left <= right:
            total += self.nums[left]
            left += 1

        return total