class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node, comp):
            if node in visited:
                return
            visited.add(node)
            comp.append(node)
            for i in graph[node]:
                dfs(i, comp)
        c = 0
        for node in range(n):
            if node in visited:
                continue
            comp = []
            dfs(node, comp)
            size = len(comp)
            edges_count = 0
            for u in comp:
                edges_count += len(graph[u])
            edges_count //= 2
            if edges_count == size*(size-1)//2:
                c += 1
        return c