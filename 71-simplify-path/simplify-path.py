class Solution(object):

    def simplifyPath(self, path):

        folders = path.split('/')
        stack = []

        for part in folders:

            if part == "" or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)