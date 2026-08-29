class Solution(object):
    def majorityElement(self, nums):
        map = {}
        for ele in nums:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1
        ans = []
        for key in map.keys():
            if map[key] > len(nums)/3:
                ans.append(key)
        return ans
        