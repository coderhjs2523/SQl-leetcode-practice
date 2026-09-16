class Solution(object):
    def backspaceCompare(self, s, t):
        stack_s = []
        stack_t = []
        
        for ele in s:
            if ele == '#':
                if stack_s: 
                    stack_s.pop()
            else:
                stack_s.append(ele)
        
        for ele in t:
            if ele == '#':
                if stack_t: 
                    stack_t.pop()
            else:
                stack_t.append(ele)

        return stack_s == stack_t
