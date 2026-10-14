class Solution(object):
    def strStr(self, haystack, needle):
        
        window_size = len(needle)
        j = 0

        for i in range(len(haystack)):

            if (i-j+1) == window_size:

                p1 = j
                p2 = 0
                flag = True

                while p1 <= i:

                    if  haystack[p1] != needle[p2]:
                        flag = False
                        break
                    p1 += 1
                    p2 += 1
                
                if flag == True:
                    return j
                
                j += 1

        return -1