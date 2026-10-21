class Solution(object):
    def makeGood(self, s):

        stack = []

        for i in range(len(s)):
            if stack and stack[-1] != s[i]:
                if stack[-1].lower() == s[i].lower():
                    stack.pop()
                    continue
            stack.append(s[i])  

        return ''.join(stack)