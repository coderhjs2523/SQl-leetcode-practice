class Solution(object):
    def removeDuplicates(self, s, k):

        stack = []

        for ele in s:

            if stack and stack[-1][0] == ele:
                item = stack.pop()
                stack.append((item[0], item[1]+1))

            else:   
                stack.append((ele, 1))

            if stack and stack[-1][1] == k:
                stack.pop()

        ans = []

        for char, count in stack:
            ans.append(char * count)

        return ''.join(ans)
        
        # ans = ""
        # while stack:
        #     item = stack.pop()
        #     ans = item[0] * item[1] + ans

        # return ans