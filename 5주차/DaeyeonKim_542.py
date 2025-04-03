import copy
from collections import deque
class Solution(object):
    def search(self, mat, start):
        queue = deque([start])
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        visited = [[0] * len(mat[0]) for _ in range(len(mat))]
        vx, vy, count = start
        visited[vx][vy] = 1

        while queue:
            x, y, count = queue.popleft()
            visited[x][y] = 1
            if mat[x][y] == 0:
                return count
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and nx < len(mat) and ny >= 0 and ny < len(mat[0]): #범위체크
                    if not visited[nx][ny]:
                        queue.append((nx,ny, count+1))

    def updateMatrix(self, mat):
        #TIME LIMIT EXCEEDED (37/50 passed)
        answer = copy.deepcopy(mat)
        for i, row in enumerate(mat): #시작 좌표
            for j, element in enumerate(row):
                if element == 1:
                    answer[i][j] = self.search(mat, (i,j,0))

        return answer
