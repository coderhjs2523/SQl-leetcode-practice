class Solution(object):
    def frequencySort(self, s):
        map = {}
        for key in s:
            if key in map:
                map[key] += 1
            else:
                map[key] = 1
        result = list(map.items())
        result.sort(key=lambda x: x[1], reverse=True)

        str = ''
        for index in range(len(result)):
            value = result[index][0]
            freq = result[index][1]
            for i in range(freq):
                str = str + value
        return str