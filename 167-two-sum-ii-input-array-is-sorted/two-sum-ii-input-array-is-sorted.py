class Solution(object):
    def twoSum(self, numbers, target):
        
        start = 0
        end = len(numbers)-1

        while start < end:
            num = numbers[start] + numbers[end]
            if num == target:
                return[start+1,end+1]
            elif num > target:
                end = end - 1
            else:
                start = start + 1
       