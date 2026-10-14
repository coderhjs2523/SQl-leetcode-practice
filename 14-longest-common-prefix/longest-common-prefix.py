class Solution(object):
    def longestCommonPrefix(self, strs):
        
        ans = strs[0]
        temp = ""

        for ele in strs:

            p1 = 0
            p2 = 0

            while p1 < len(ans) and p2 < len(ele):

                if ans[p1] != ele[p2]:
                   break

                temp += ans[p1]
                p1 += 1
                p2 += 1

            ans = temp
            temp = ""

        return ans