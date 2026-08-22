class Solution(object):
    def uniqueOccurrences(self, arr):
        
        map = {}

        for num in arr:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        count = set()

        for key in map:
            if map[key] in count:
                return False
            count.add(map[key])
        return True
        