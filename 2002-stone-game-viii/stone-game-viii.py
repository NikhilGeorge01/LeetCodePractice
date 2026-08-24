class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        cumsum = [0]
        for x in stones:
            cumsum.append(cumsum[-1] + x)
        @cache
        def dfs(i):
            if i == len(stones):
                return cumsum[-1]
            return max(cumsum[i] - dfs(i + 1), dfs(i + 1))
        return dfs(2)