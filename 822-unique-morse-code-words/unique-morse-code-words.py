class Solution(object):
    def uniqueMorseRepresentations(self, words):
        
        MORSE_CODE = {
        'a': '.-',     'b': '-...',   'c': '-.-.',   'd': '-..',    'e': '.',
        'f': '..-.',   'g': '--.',    'h': '....',   'i': '..',     'j': '.---',
        'k': '-.-',    'l': '.-..',   'm': '--',     'n': '-.',     'o': '---',
        'p': '.--.',   'q': '--.-',   'r': '.-.',    's': '...',    't': '-',
        'u': '..-',    'v': '...-',   'w': '.--',    'x': '-..-',   'y': '-.--',
        'z': '--..'}
        
        ans = set()

        for i in words:
            temp = ""
            for ch in i:
                temp += MORSE_CODE[ch]
            ans.add(temp)

        return len(ans) 