import copy
class Solution(object):
    def dfs(self, start, grid, answer, count):
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        x, y = start
        answer[x][y] = count
        print("visiting : ", start)
        for i in range (4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]): 
                if answer[nx][ny] == 0 and grid[nx][ny] == 1:
                    answer[nx][ny] = count
                    self.dfs((nx, ny), grid, answer, count)

    def numIslands(self, grid):
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if grid[i][j] == "1":
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0

        answer = [[0] * len(grid[0]) for _ in range(len(grid))]
        count = 0 #island number
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if grid[i][j] == 1 and answer[i][j] == 0:
                    print(i,j)
                    count += 1
                    self.dfs((i,j), grid, answer, count)
                    
        return count
        