class Solution(object):
    def removeDuplicates(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j], nums[i] =  nums[i], nums[j]
        return j+1
        