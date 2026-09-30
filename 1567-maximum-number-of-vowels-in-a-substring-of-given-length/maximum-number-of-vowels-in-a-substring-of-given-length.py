class Solution(object):
    def maxVowels(self, s, k):
        count = 0
        ans = 0
        j = 0

        for i in range(len(s)):
            if s[i] in "aeiou":
                count += 1
            
            if i-j+1 == k:
                ans = max(ans, count)
                if s[j] in "aeiou":
                    count -= 1
                j += 1

        return ans