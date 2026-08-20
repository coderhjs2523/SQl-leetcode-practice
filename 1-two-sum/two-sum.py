class Solution(object):
    def twoSum(self, nums, target):
        
        map = {}

        for i in range(len(nums)):
            value = target-nums[i]
            if value in map.keys():
                return[i,map[value]]
            map[nums[i]] = i
