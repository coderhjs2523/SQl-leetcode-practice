class Solution(object):
    def longestBeautifulSubstring(self, word):
        
        l = 0
        ans = 0
        vowel_count = 1

        for r in range(1,len(word)):

            if word[r] >= word[r-1]:
                if word[r] > word[r-1]:
                    vowel_count += 1

                if vowel_count == 5:
                    ans = max(ans, r-l+1)
            else:
                vowel_count = 1
                l = r

        return ans