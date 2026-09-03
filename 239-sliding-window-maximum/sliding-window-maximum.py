# from collections import deque
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        dq = deque()
        result = []

        for i in range(len(nums)):

            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

        
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):

#         window = deque()
#         result = []

#         for i in range(k):
#             window.append(nums[i])

#         maxnum = max(window)
#         result.append(maxnum)

#         for i in range(k,len(nums)):
            
#             left = window.popleft()
#             window.append(nums[i])

#             if left == maxnum:
#                 maxnum = max(window)
            
#             maxnum = max(maxnum, nums[i])
#             result.append(maxnum)

#         return result