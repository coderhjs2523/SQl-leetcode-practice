class Solution(object):
    def findTheDifference(self, s, t):
        
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
        
        for ele in mapt.keys():
            if ele in maps:
                if maps[ele] != mapt[ele]:
                    return ele
            else:
                return ele