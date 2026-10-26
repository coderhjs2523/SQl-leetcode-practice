# class Solution(object):
#     def decodeString(self, s):
        
#         stack_num = []
#         stack_alp = []
#         num = 0

#         for ch in s:

#             if ch.isdigit():
#                 num = num * 10 + int(ch)
#                 continue

#             elif ch == '[':
#                 stack_num.append(num)
#                 num = 0

#             elif ch == ']':
#                 temp = ""

#                 while stack_alp[-1] != '[':
#                     temp = stack_alp.pop() + temp
#                 stack_alp.pop()
#                 stack_alp.append(temp * stack_num.pop())
#                 continue

#             stack_alp.append(ch)

#         return "".join(stack_alp)



class Solution(object):
    def decodeString(self, s):
        stack_num = []
        stack_alp = []
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack_num.append(num)
                stack_alp.append(ch)
                num = 0

            elif ch == ']':
                temp = []

                while stack_alp[-1] != '[':
                    temp.append(stack_alp.pop())

                stack_alp.pop()
                temp.reverse()

                stack_alp.append(''.join(temp) * stack_num.pop())

            else:
                stack_alp.append(ch)

        return ''.join(stack_alp)
