class Solution(object):
    def isAnagram(self, s, t):
        
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
        
        if len(t)>len(s):
            for ele in mapt.keys():
                if ele not in maps:
                    return False
                else:
                    if mapt[ele] != maps[ele]:
                        return False
            return True

        else:
            for ele in maps.keys():
                if ele not in mapt:
                    return False
                else:
                    if maps[ele] != mapt[ele]:
                        return False
            return True