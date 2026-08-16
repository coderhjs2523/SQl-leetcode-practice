class Solution(object):
    def lengthOfLongestSubstring(self, s):

        Set = set()
        j = 0
        maxlength = 0

        for i in range(len(s)):

            if s[i] in Set:

                length = i - j
                maxlength = max(maxlength, length)

                while s[j] != s[i]:
                    Set.remove(s[j])
                    j += 1

                Set.remove(s[j])
                j += 1

            Set.add(s[i])

        length = len(s) - j
        maxlength = max(maxlength, length)

        return maxlength