class Solution(object):
    def intersection(self, nums1, nums2):
        
        SET = set()
        ans = []

        if len(nums1) > len(nums2):
            for ele in nums1:
                SET.add(ele)

            for ele in nums2:
                if ele in SET:
                    ans.append(ele)
                    SET.remove(ele)

        else:
            for ele in nums2:
                SET.add(ele)

            for ele in nums1:
                if ele in SET:
                    ans.append(ele)
                    SET.remove(ele)
        return ans
        