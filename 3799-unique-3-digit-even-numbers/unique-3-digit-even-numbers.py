class Solution(object):
    def totalNumbers(self, digits):
        
        ans = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if digits[i] == 0 or digits[k]%2 == 1 or (i==j or j==k or k==i):
                        continue
                    ans.add(digits[i]*100 + digits[j]*10 + digits[k])
        return len(ans)