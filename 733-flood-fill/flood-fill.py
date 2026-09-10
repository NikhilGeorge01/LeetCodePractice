class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startcolor = image[sr][sc]
        if startcolor == color:
            return image
        def dfs(i,j):
            if not (image[i][j] == startcolor):
                return
            dirn = [[1,0], [0,1],[-1,0],[0,-1]]
            image[i][j] = color
            for a,b in dirn:
                ni,nj = a+i,b+j
                if 0<= ni < len(image) and 0 <= nj < len(image[0]):
                    dfs(ni,nj)
        dfs(sr,sc)
        return image

        