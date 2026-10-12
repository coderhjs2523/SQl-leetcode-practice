class Solution(object):
    def characterReplacement(self, s, k):

        map = {}
        count = 0
        j = 0
        ans = 0

        for i in range(len(s)):
            
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1

            count = max(count, map[s[i]])

            while (i - j + 1) - count > k:
                map[s[j]] -= 1
                j += 1

            ans = max(ans, i - j + 1)

        return ans