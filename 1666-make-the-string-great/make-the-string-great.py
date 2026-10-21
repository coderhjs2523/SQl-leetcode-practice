class Solution(object):
    def makeGood(self, s):

        stack = []

        for ele in s:
            if stack and stack[-1] != ele:
                if stack[-1].lower() == ele.lower():
                    stack.pop()
                    continue
            stack.append(ele)  

        return ''.join(stack)