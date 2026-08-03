class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dfs(i):
            if i >= len(stoneValue):
                return 0
            take1 = stoneValue[i] - dfs(i+1)
            take2 = float('-inf')
            if i+1 < len(stoneValue):
                take2 = stoneValue[i] + stoneValue[i+1] - dfs(i+2)
            take3 = float('-inf')
            if i+2 < len(stoneValue):
                take3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dfs(i+3)
            return max(take1, take2, take3)
        res = dfs(0)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"