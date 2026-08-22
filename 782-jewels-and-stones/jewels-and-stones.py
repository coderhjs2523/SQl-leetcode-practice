class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        
        map = {}
        for ch in stones:
            if ch in map.keys():
                map[ch] += 1
            else:
                map[ch] = 1
        
        count = 0
        for elekey in jewels:
            if elekey in map.keys():
                count += map[elekey]
        return count