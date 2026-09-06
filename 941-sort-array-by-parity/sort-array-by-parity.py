class Solution(object):
    def sortArrayByParity(self, nums):
       
        j = -1

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                j += 1
                nums[i],nums[j] = nums[j], nums[i]
        return nums
        