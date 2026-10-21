class Solution(object):
    def backspaceCompare(self, s, t):
        s_stack = []
        t_stack = []

        for ele in s:
            if ele == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(ele)
        
        for ele in t:
            if ele == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(ele)

        return s_stack == t_stack