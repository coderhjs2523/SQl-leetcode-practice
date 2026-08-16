class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        n1 = m - 1
        n2 = n - 1
        p = m + n - 1

        while n1>=0 and n2>=0:
            if nums1[n1]>nums2[n2]:
                nums1[p]=nums1[n1]
                n1 = n1 - 1
                p = p - 1
            else:#nums2[n1]>nums1[n2]
                nums1[p]=nums2[n2]
                n2 = n2 - 1
                p = p - 1
        while n1>=0:
            nums1[p]=nums1[n1]
            n1 = n1 - 1
            p = p - 1
        while n2>=0:
            nums1[p]=nums2[n2]
            n2 = n2 - 1
            p = p - 1
        return nums1