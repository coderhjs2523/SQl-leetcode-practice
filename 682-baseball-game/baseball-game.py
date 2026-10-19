class Solution(object):
    def calPoints(self, operations):

        stack = []
        
        for ch in operations:
            if ch == '+':
                stack.append(stack[-1] + stack[-2])
            elif ch == 'D':
                stack.append(stack[-1]*2)
            elif ch == 'C':
                stack.pop()
            else:
                stack.append(int(ch))
        
        return sum(stack)
        
        # stack = []

        # for ch in operations:

        #     if ch in '+DC':

        #         if not stack:
        #             continue

        #         elif ch == '+':
        #             if len(stack) < 2:
        #                 stack.append(stack[-1])
        #             else:
        #                 stack.append(stack[-1] + stack[-2])

        #         elif ch == 'D':
        #             stack.append(stack[-1]*2)

        #         elif ch == 'C':
        #             stack.pop()

        #     else:
        #         stack.append(int(ch))
        
        # return sum(stack)