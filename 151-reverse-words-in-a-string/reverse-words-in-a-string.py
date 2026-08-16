class Solution(object):
    def reverseWords(self, s):
        list = s.split()
        ans = ""
        for ele in list:
            ans = ele + " " + ans
            
        return ans.strip()
        