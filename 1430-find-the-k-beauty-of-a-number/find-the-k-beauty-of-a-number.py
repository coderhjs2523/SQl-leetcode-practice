class Solution(object):
    def divisorSubstrings(self, num, k):
        
        term = num
        arr = []

        while term != 0:
            r = term % 10
            arr.append(r)
            term = term / 10

        arr.reverse()

        l = 0
        divisor = 0
        ans = 0

        for r in range(len(arr)):
            divisor = (divisor * 10) + arr[r]
            if (r - l + 1) == k:
                if divisor != 0 and (num % divisor) == 0:
                    ans += 1
                divisor = divisor - (arr[l] * 10**(k-1))
                l += 1

        return ans