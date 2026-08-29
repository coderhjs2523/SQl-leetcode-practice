class Solution(object):
    def findRepeatedDnaSequences(self, s):

        repeat_set = set()
        check_set = set()

        for i in range(len(s) - 9):

            temp_str = s[i:i + 10]

            if temp_str in check_set:
                repeat_set.add(temp_str)
            else:
                check_set.add(temp_str)

        return list(repeat_set)