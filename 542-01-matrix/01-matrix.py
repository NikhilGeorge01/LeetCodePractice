class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        temp = [row[:] for row in mat]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                else:
                    temp[i][j] = float('inf')
        dirn = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            i,j,d = q.popleft()
            if temp[i][j] < d:
                continue
            temp[i][j] = d
            for x,y in dirn:
                ni = i+ x
                nj = j + y
                if ni in range(len(mat)) and nj in range(len(mat[0])):
                    q.append((ni,nj,d + 1))
        return temp
             
