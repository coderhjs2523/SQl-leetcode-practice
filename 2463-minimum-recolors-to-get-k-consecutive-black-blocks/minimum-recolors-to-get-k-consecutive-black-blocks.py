class Solution(object):
    def minimumRecolors(self, blocks, k):
        count_white = 0

        l = 0
        ans = float('inf')

        for r in range(len(blocks)):

            if blocks[r] == 'W':
                count_white += 1

            if (r-l+1) == k:
                ans = min(ans, count_white)
                if blocks[l] == 'W':
                    count_white -= 1
                l += 1
                
        return ans