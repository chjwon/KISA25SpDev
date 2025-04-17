from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        n, m = len(grid), len(grid[0])
        queue = deque()
        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        while queue:
            x, y ,time = queue.popleft()
            answer = max(answer, time)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx,ny,time+1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: #fresh orange exists
                    return -1
        return answer