class Solution(object):
    def maxSum(self, nums, m, k):
        
        map = {}
        l = 0
        sum = 0
        ans = 0

        for r in range(len(nums)):

            if nums[r] in map:
                map[nums[r]] += 1
            else:
                map[nums[r]] = 1

            sum += nums[r]

            if (r-l+1) == k:
                if len(map) >= m:
                    ans = max(ans, sum)
                
                sum -= nums[l]

                map[nums[l]] -= 1

                if map[nums[l]] == 0:
                    del(map[nums[l]])
                
                l += 1
        
        return ans