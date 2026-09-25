class Solution(object):
    def singleNumber(self, nums):
        # map = {}

        # for ele in nums:
        #     if ele in map:
        #         map[ele] += 1
        #     else:
        #         map[ele] = 1
        
        # for key in map.keys():
        #     if map[key] == 1:
        #         return key

        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans