class Solution(object):
    def sortColors(self, nums):
        
        start = 0
        end = len(nums)-1
        p = 0
        while p<=end:
            if nums[p] == 0:
                nums[start],nums[p] = nums[p],nums[start]
                p += 1
                start += 1
            elif nums[p] == 2:
                nums[end],nums[p] = nums[p],nums[end]
                end -= 1
            else:
                p = p+1
        return nums
        