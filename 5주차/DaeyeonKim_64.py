class Solution(object):
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        answer = [[0] * m for _ in range(n)]
        answer[0][0] = grid[0][0]
        for i in range(1, n):
            answer[i][0] = answer[i-1][0] + grid[i][0]
        for j in range(1, m):
            answer[0][j] = answer[0][j-1] + grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                answer[i][j] = min(answer[i-1][j],answer[i][j-1]) + grid[i][j]

        return answer[n-1][m-1]