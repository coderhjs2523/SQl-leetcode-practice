class Solution(object):
    def majorityElement(self, nums):
        
        map = {}

        for ele in nums:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1
        
        for ele in map.keys():
            if map[ele] > len(nums)/2:
                return ele
        