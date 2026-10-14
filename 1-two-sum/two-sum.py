class Solution(object):
    def twoSum(self, nums, target):
        
        map = {}

        for i in range(len(nums)):

            find = target - nums[i]

            if find in map:
                return[map[find], i]
            
            map[nums[i]] = i
        