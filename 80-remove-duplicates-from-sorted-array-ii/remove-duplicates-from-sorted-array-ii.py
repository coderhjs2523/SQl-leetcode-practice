class Solution(object):
    def removeDuplicates(self, nums):

        k = 0

        for i in range(len(nums)):
            if k<2 or nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1

        return k