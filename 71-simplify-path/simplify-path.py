class Solution(object):
    def simplifyPath(self, path):
        
        items = path.split('/')
        stack = []

        for ele in items:

            if ele == "" or ele == '.':
                continue
            elif ele == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ele)
        
        return "/" + "/".join(stack)