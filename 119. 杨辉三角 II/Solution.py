class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        res = [[1]]
        for _ in range(1, rowIndex+1):
            last_line = res[-1]
            temp = [1]
            for idx in range(1, len(last_line)):
                temp.append(last_line[idx-1]+last_line[idx])
            temp.append(1)
            res.append(temp)
        return res[-1]