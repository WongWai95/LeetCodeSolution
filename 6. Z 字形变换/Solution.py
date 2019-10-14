class Solution:
    def convert(self, s: str, numRows: int) -> str:
        split_result = ['' for _ in range(numRows)]
        
        direction = 1
        mark = [0]
        for i in range(1, 2*numRows-2):
            mark.append(mark[i-1] + direction)
            if mark[-1] == numRows - 1:
                direction = -1

        for index in range(len(s)):
            try:
                remain = index % (2*numRows-2)
            except ZeroDivisionError:
                remain = 0
            split_result[mark[remain]] += s[index]
            
        result = ''
        for i in range(numRows):
            result += split_result[i]
            
        return result