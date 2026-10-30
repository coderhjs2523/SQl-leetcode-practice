class Solution(object):
    def numberOfLines(self, widths, s):
        
        count_line = 1
        sum_pixel = 0

        for i in s:
            char_width = widths[ord(i) - ord('a')]
            
            if sum_pixel + char_width > 100:
                count_line += 1
                sum_pixel = char_width 
            else:
                sum_pixel += char_width 
        
        return [count_line, sum_pixel]
