class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in range(len(isConnected)):
                if isConnected[node][i] == 1:
                    dfs(i)
        visited = set()
        p = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            p += 1
            dfs(i)
        return p

