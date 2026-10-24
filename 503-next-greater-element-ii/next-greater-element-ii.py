class Solution(object):
    def nextGreaterElements(self, nums):
        
        stack = []
        n= len(nums)
        ans = [-1]*n

        for i in range(2*n-1, -1, -1):

            idx = i % n

            while stack and nums[idx] >= stack[-1]:
                stack.pop()

            if stack:
                ans[idx] = stack[-1]

            stack.append(nums[idx])

        return ans