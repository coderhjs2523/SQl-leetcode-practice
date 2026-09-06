class Solution(object):
    def reverseOnlyLetters(self, s):
        
        s = list(s)
        start = 0
        end = len(s)-1

        while start < end:
            if not s[start].isalpha():
                start += 1
                continue
            
            if not s[end].isalpha():
                end -= 1
                continue

            s[start], s[end] = s[end], s[start]

            start += 1
            end -= 1

        return "".join(s)