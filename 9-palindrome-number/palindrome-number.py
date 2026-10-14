class Solution(object):
    def isPalindrome(self, x):
        
        if x < 0:
            return False

        temp = 0
        copy = x

        while copy !=0:
            r = copy % 10
            temp = temp * 10 + r
            copy = copy / 10

        if temp == x:
            return True
        
        return False