class Solution(object):
    def isAnagram(self, s, t):
        
        map1 = {}
        map2 = {}

        for ele in s:
            
            if ele in map1:
                map1[ele] += 1
            else:
                map1[ele] = 1

        for ele in t:
            
            if ele in map2:
                map2[ele] += 1
            else:
                map2[ele] = 1

        return map1 == map2