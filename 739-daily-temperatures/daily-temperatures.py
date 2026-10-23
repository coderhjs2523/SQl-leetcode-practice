class Solution(object):
    def dailyTemperatures(self, temperatures):


        stack = []
        ans = [0]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):

            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i
            
            stack.append(i)
        
        return ans
        
        # stack = []
        # map = {}

        # ans = [0]*len(temperatures)

        # for i in range(len(temperatures)-1, -1, -1):

        #     map[temperatures[i]] = i
           
        #     while stack and temperatures[i] >= stack[-1]:
        #         stack.pop()
            
        #     if not stack:
        #         ans[i] = 0
        #     else:
        #         ans[i] = map[stack[-1]] - i
            
        #     stack.append(temperatures[i])

        # return ans