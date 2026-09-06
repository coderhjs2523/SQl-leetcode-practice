class Solution(object):
    def topKFrequent(self, words, k):
        
        map = {}

        for key in words:
            if key in map:
                map[key] += 1
            else:
                map[key] = 1

        ans = []

        while k > 0:
            max_freq = -1
            temp = ""

            for key in map.keys():
                current_freq = map[key]

                if current_freq > max_freq:
                    temp = key
                    max_freq = current_freq
                
                elif current_freq == max_freq:
                    if key < temp:
                        temp = key
            
            ans.append(temp)
            map.pop(temp)
            k -= 1
        
        return ans
