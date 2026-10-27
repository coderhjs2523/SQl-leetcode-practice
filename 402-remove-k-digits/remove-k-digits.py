
class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for ele in num:
            while stack and k > 0 and ele < stack[-1]:
                stack.pop()
                k -= 1

            if len(stack) == 0 and ele == '0':
                continue

            stack.append(ele)

        if k > 0:
            stack = stack[:-k]

        return ''.join(stack) or '0'
