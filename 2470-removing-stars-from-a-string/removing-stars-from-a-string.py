class Solution(object):
    def removeStars(self, s):
        
        stack = []

        for ele in s:

            if ele == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(ele)

        return ''.join(stack)    