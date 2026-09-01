class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        map1 = {}
        map2 = {}

        for num1 in nums1:
            for num2 in nums2:
                if (num1 + num2) in map1: 
                    map1[num1 + num2] += 1
                else:
                    map1[num1 + num2] = 1
            

        for num3 in nums3:
            for num4 in nums4:
                if (num3 + num4) in map2: 
                    map2[num3 + num4] += 1
                else:
                    map2[num3 + num4] = 1  

        ans = 0
        for ele in map1.keys():
            if (-ele) in map2:
                ans += map1[ele] * map2[-ele]

        return ans      