class Solution(object):
    def isValid(self, s):
        
        stack = []
        check = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            if ch in check:
                if not stack or stack.pop() != check[ch]:
                    return False
        return not stack