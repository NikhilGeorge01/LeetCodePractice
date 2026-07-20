class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        new = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                newidx = (idx + k) % (m * n)
                newrow = newidx // n
                newcol = newidx % n
                new[newrow][newcol] = grid[i][j]
        return new