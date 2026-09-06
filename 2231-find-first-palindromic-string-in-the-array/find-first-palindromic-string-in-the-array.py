class Solution(object):
    def firstPalindrome(self, words):
        
        for ele in words:
            start = 0
            end = len(ele)-1
            flag = True

            while start < end:
                if ele[start] != ele[end]:
                    flag = False
                    break
                start += 1
                end -= 1
            
            if flag:
                return ele
        
        return ""
        