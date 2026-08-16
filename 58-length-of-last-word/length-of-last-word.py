class Solution(object):
    def lengthOfLastWord(self, s):
        end = len(s)-1
        while not s[end].isalnum():
            end -= 1
        if end < 0:
            return 0
        count = 0
        while end>=0 and s[end].isalnum():
            count += 1
            end -= 1
        return count 