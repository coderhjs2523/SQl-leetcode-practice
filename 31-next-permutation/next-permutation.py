class Solution(object):
    def swap(self, nums, start, end):
        while start<end:
            nums[start],nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums

    def nextPermutation(self, nums):
        pivot = -1
        index = -1
        n= len(nums)-1

        for i in range(n,0,-1):
            if(nums[i]>nums[i-1]):
                pivot = nums[i-1]
                index = i-1
                break
        
        if(pivot == -1):
            self.swap(nums,0,n)
            return
        

        for i in range(n,index,-1):
            if(nums[i] > nums[index]):
                nums[i],nums[index] = nums[index], nums[i]
                break
        
        self.swap(nums, index+1, n)