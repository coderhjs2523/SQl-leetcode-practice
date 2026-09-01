class Solution(object):
    def topKFrequent(self, nums, k):
        
        map = {}

        for ele in nums:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1
        
        ans = []
        for i in range(k):
            maxele = -1
            fillele = -1
            for key in map.keys():
                if map[key] > maxele:
                    maxele = map[key]
                    fillele = key
            ans.append(fillele)
            map.pop(fillele)
        return ans