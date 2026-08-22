class Solution(object):
    def sumOfUnique(self, nums):
        map = {}
        for ele in nums:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1

        sum = 0
        for key in map.keys():
            if map[key] == 1:
                sum += key
        return sum