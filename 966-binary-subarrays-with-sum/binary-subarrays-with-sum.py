class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        
        map = {}
        map[0] = 1

        ans = 0
        prefix = 0

        for ele in nums:

            prefix += ele

            if (prefix - goal) in map:
                ans += map[prefix - goal]
            
            if prefix in map:
                map[prefix] += 1
            else:
                map[prefix] = 1
        
        return ans
        