class Solution(object):
    def subarraySum(self, nums, k):
        
        map = {}
        map[0] = 1
        
        prefix_sum = 0
        ans = 0

        for ele in nums:

            prefix_sum += ele
            find = prefix_sum - k
            
            if find in map:
                ans += map[find]

            if prefix_sum in map:
                map[prefix_sum] += 1
            else:
                map[prefix_sum] = 1
        
        return ans