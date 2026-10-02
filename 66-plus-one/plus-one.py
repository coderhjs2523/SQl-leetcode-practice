class Solution(object):
    def plusOne(self, digits):

        num = 0
        for ele in digits:
            num = num*10 + ele

        num = num + 1
        ans = []

        while num != 0:
            r = num % 10
            ans.append(r)
            num = num / 10
        
        ans.reverse()
        return ans