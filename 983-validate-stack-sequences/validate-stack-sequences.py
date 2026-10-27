class Solution(object):
    def validateStackSequences(self, pushed, popped):
        
        stack = []
        i = 0
        for ele in pushed:

            stack.append(ele)

            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return len(stack) == 0