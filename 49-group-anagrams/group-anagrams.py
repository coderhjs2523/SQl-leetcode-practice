class Solution(object):
    def groupAnagrams(self, strs):
        
        map = {}

        for ele in strs:

            key_item = str(sorted(ele))

            if key_item not in map:
                map[key_item] = []
            
            map[key_item].append(ele)

        return map.values()