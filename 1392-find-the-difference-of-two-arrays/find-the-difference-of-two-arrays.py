class Solution(object):
    def findDifference(self, nums1, nums2):
        set1 = set()
        set2 = set()
       
        ans = []

        for ele in nums1:
            set1.add(ele)
        for ele in nums2:
            set2.add(ele)

        list1 = []
        for ele in set1:
            if ele not in set2:
                list1.append(ele)

        ans.append(list1)

        list2 = []
        for ele in set2:
            if ele not in set1:
                list2.append(ele)
                
        ans.append(list2)
        
        return ans