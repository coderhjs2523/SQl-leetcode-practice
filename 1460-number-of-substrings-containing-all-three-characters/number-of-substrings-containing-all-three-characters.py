class Solution(object):
    def numberOfSubstrings(self, s):

        map = {}
        ans = 0
        j = 0
        
        for i in range(len(s)):

            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1

            while(len(map) == 3):
                ans += len(s) - i

                map[s[j]] -= 1

                if map[s[j]] == 0:
                    del(map[s[j]])

                j += 1
        
        return ans