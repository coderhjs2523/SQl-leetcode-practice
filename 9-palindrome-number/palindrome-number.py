class Solution(object):
    def isPalindrome(self, x):
        
        if x<0:
            return False
        copy = x
        num = 0
        while x!=0:
            num = num*10 + x%10
            x = x/10
        if copy == num:
            return True
        return False
        