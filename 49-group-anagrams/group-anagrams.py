class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        for s in strs:
            key = str(sorted(s))
            if key not in map:
                map[key] = list()
            map[key].append(s)
        return map.values() 
        