class Solution(object):
    def validateStackSequences(self, pushed, popped):
        
        stack = []
        i = 0
        for ele in pushed:

            if ele == popped[i]:
                i += 1
                while stack and stack[-1] == popped[i]:
                    stack.pop()
                    i += 1
                continue

            stack.append(ele)

        return len(stack) == 0