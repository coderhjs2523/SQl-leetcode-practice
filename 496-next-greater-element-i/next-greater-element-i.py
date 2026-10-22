class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        map = {}

        for i in range(len(nums2)-1,-1,-1):

            while stack and nums2[i] >= stack[-1]:
                stack.pop()

            if not stack:
                map[nums2[i]] = -1
            else:
                map[nums2[i]] = stack[-1]

            stack.append(nums2[i])
               
        ans = []

        for ele in nums1:
            ans.append(map[ele])

        return ans