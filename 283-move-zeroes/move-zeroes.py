class Solution(object):
    def moveZeroes(self, nums):
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(nums[i])

        while len(ans) < len(nums):
            ans.append(0)

        for i in range(len(nums)):
            nums[i] = ans[i]
        
        return nums
        
        