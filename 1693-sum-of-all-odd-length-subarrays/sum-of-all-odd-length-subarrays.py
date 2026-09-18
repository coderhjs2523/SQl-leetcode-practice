class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        
        n = len(arr)

        prefix = [0]*n
        prefix[0] = arr[0]

        for i in range(1,n):
            prefix[i] = prefix[i-1] + arr[i]

        ans = 0
        for i in range(0,n):
            for j in range(i,n):
                if (j-i+1) % 2 == 1:
                    if(i==0):
                        ans += prefix[j]
                    else:
                        ans += prefix[j] - prefix[i-1]
        return ans