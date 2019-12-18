class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        res = [[1]]
        for _ in range(1, numRows):
            last_line = res[-1]
            temp = [1]
            for idx in range(1, len(last_line)):
                temp.append(last_line[idx-1]+last_line[idx])
            temp.append(1)
            res.append(temp)
        return res