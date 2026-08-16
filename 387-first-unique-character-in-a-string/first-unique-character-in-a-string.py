class Solution(object):
    def firstUniqChar(self, s):
        
        map = {}
        for ele in s:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1
        for i in range(len(s)):
            ele = s[i]
            freq = map[ele]
            if freq == 1:
                return i
        return -1
        