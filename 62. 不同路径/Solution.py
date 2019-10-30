class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 0: return 0
        # DP 算法，记忆表初始化
        table = [[None for _ in range(n)] for _ in range(m)]

        # 赋初值
        for i in range(n):
            table[-1][i] = 1
        for i in range(m):
            table[i][-1] = 1
        
        # 递推
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                table[row][col] = table[row+1][col] + table[row][col+1]
                
        # 结果
        return table[0][0]