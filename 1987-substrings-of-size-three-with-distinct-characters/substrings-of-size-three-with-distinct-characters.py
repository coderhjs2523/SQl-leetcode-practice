class Solution(object):
    def countGoodSubstrings(self, s):

        map = {}

        j = 0
        ans = 0

        for i in range(len(s)):

            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1

            if i-j+1 == 3:
                if len(map) == 3:
                    ans += 1

                map[s[j]] -= 1    

                if map[s[j]] == 0:
                    del map[s[j]]

                j += 1
        
        return ans