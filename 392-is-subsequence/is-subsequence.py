class Solution(object):
    def isSubsequence(self, s, t):
        
        p1 = 0
        p2 = 0
        if s == "":
             return True
        while p1<len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 = p1 + 1
                if p1 == len(s):
                    return True
            p2 = p2 + 1
        return False 
    