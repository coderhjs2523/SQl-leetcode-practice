class Solution(object):
    def isValid(self, s):

        stack = []
        check = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for ch in s:

            if ch in "([{":
                stack.append(ch)       

            elif ch in check:
                if not stack:
                    return False
                if check[ch] != stack.pop():
                    return False

        return len(stack) == 0