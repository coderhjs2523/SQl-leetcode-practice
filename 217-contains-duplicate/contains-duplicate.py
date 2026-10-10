class Solution(object):
    def containsDuplicate(self, nums):
        check = set()

        for ele in nums:
            if ele in check:
                return True
            check.add(ele)
        return False