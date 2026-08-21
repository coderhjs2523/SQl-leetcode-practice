class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        map1 = {}
        map2 = {}

        for ele in ransomNote:
            if ele in map1.keys():
                map1[ele] += 1
            else:
                map1[ele] = 1

        for ele in magazine:
            if ele in map2.keys():
                map2[ele] += 1
            else:
                map2[ele] = 1
        
        for key in map1.keys():
            if key not in map2.keys():
                return False
            if map1[key] > map2[key]:
                return False
        return True
