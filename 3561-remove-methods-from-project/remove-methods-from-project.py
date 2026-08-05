class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in invocations:
            adj[a].append(b)
        visited = set()
        def invoke(x):
            if x in visited:
                return
            visited.add(x)
            for edj in adj[x]:
                invoke(edj)
        invoke(k)
        for a, b in invocations:
            if a not in visited and b in visited:
                return list(range(n))
        op = []
        for i in range(n):
            if i not in visited:
                op.append(i)
        return op