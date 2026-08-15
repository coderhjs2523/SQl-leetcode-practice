class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        self.rotateByHalfs(0, n-1, nums)
        self.rotateByHalfs(0, k-1, nums)
        self.rotateByHalfs(k, n-1, nums)
    
    def rotateByHalfs(self, start, end, nums):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

            start += 1
            end -= 1
        