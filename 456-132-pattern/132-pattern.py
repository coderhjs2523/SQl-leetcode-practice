class Solution(object):
    def find132pattern(self, nums):
        
        stack = [] #num2
        num3 = -float('inf')

        for i in range(len(nums)-1, -1, -1):
            num1 = nums[i]
            if num1 < num3:
                return True
            
            while stack and num1 > stack[-1]:
               num3 = stack.pop()

            stack.append(num1)
        
        return False