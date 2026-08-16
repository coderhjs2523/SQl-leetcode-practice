class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        
        window = 0
        for i in range(k):
            window += arr[i]
        
        count = 0
        if window/k >= threshold:
            count += 1
        
        start = 0
        end = k
        while end < len(arr):

            window -= arr[start]
            start += 1

            window += arr[end]
            end += 1

            if window/k >= threshold:
                count += 1

        return count        