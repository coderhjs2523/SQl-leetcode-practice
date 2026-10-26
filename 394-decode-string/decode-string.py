class Solution(object):
    def decodeString(self, s):
        
        stack_num = []
        stack_alp = []
        num = 0

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)
                continue

            elif ch == '[':
                stack_num.append(num)
                num = 0

            elif ch == ']':

                flag = True
                temp = ""

                while flag:

                    item = stack_alp.pop()

                    if item == '[':
                        break

                    temp = item + temp

                stack_alp.append(temp * stack_num.pop())
                continue

            stack_alp.append(ch)

        return "".join(stack_alp)