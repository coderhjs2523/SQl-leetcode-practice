class Solution(object):
    def isSubsequence(self, s, t):
        
        p1 = 0
        p2 = 0
        count = len(s)

        while p1 < len(s) and p2 < len(t):

            if s[p1] == t[p2]:
                count -= 1
                p1 += 1
            p2 += 1
        
        return count == 0

        