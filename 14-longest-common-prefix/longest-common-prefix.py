class Solution(object):
    def longestCommonPrefix(self, strs):
        
        temp = ""
        prefix = strs[0]

        for i in range(1,len(strs)):
            s1 = strs[i]
            p1 = 0
            p2 = 0
            while p1<len(prefix) and p2<len(s1) and s1[p1] == prefix[p2]:
                temp += s1[p1]
                p1 += 1
                p2 += 1
            prefix = temp
            temp = ""
        return prefix