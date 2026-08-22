class Solution(object):
    def checkIfPangram(self, sentence):
        
        SET = set()
        for ele in sentence:
            SET.add(ele)
        if len(SET) == 26:
            return True
        return False
        