class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        sum = 0
        ans = 0
        j = 0
        for i in range(len(arr)):
            sum += arr[i]
            
            if i-j+1 == k:
                avg = sum / k
                if avg >= threshold:
                    ans += 1
                sum -= arr[j]
                j += 1
        
        return ans