class Solution(object):
    def numberOfSubarrays(self, nums, k):
        
        map = {}
        map[0] = 1

        n = len(nums)

        for i in range(n):

            if(nums[i] % 2 == 0):
                nums[i] = 0
            else:
                nums[i] = 1
            
        ans = 0
        prefix = 0

        for ele in nums:

            prefix += ele
            if (prefix-k) in map:
                ans += map[prefix-k]
            
            if prefix in map:
                map[prefix] += 1
            
            else:
                map[prefix] = 1

        return ans