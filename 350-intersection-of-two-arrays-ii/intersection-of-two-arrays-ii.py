class Solution(object):
    def intersect(self, nums1, nums2):
        
        map1 = {}
        map2 = {}
        ans = []

        for ele in nums1:
            if ele in map1:
                map1[ele] += 1
            else:
                map1[ele] = 1 
        
        for ele in nums2:
            if ele in map2:
                map2[ele] += 1
            else:
                map2[ele] = 1 
        
        for key in map1.keys():
            if key in map2.keys():
                n = min(map1[key], map2[key])
                for i in range(n):
                    ans.append(key)

        return ans