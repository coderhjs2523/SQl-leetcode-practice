
class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in ("+", "-", "*", "/"):
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    result = b + a
                elif token == "-":
                    result = b - a
                elif token == "*":
                    result = b * a
                else:
                    result = abs(b) // abs(a)

                    if ((a < 0) and (b > 0)) or ((a > 0) and (b < 0)):
                        result = result * (-1)

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]
