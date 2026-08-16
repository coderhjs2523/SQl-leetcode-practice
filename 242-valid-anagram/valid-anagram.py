class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False
        
        maps = {}
        mapt = {}

        for ele in s:
            if ele in maps:
                maps[ele] += 1
            else:
                maps[ele] = 1

        for ele in t:
            if ele in mapt:
                mapt[ele] += 1
            else:
                mapt[ele] = 1
        
        for ele in maps.keys():
            if ele not in mapt:
                return False
            else:
                if maps[ele] != mapt[ele]:
                    return False
        return True