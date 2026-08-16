class Solution(object):
    def containsDuplicate(self, nums):
        
        map = {}

        for ele in nums:
            if ele in map:
                return True
            else:
                map[ele] = 1
        return False
        