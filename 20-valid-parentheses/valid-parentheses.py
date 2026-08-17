class Solution(object):
    def isValid(self, s):
        stack = []
        pairs={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            if ch in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[ch]:
                    return False
        return len(stack) == 0