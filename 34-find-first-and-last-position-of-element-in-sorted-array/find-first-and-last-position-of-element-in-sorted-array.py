class Solution(object):
    def searchRange(self, nums, target):
        
        ans=[-1, -1]
        start = 0
        end = len(nums) - 1
        while start<=end:
            mid = (start+end)/2
            if nums[mid] == target:
                ans[0] = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        start = 0
        end = len(nums) - 1
        while start<=end:
            mid = (start+end)/2
            if nums[mid] == target:
                start = mid + 1
                ans[1] = mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return ans