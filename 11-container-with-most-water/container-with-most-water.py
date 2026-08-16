class Solution(object):
    def maxArea(self, height):
        
        start = 0
        end = len(height) - 1
        ans = 0

        while start<end:
            b = end-start
            l = min(height[start], height[end])
            volume = l*b
            ans = max(ans,volume)
            if height[start]>height[end]:
                end = end - 1
            else:
                start = start + 1
        return ans
        