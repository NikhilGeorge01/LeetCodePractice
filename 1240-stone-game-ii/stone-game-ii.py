class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs(i, M):
            if (i, M) in dp:
                return dp[(i, M)]
            if i >= len(piles):
                return 0
            sumval = 0
            best = float('-inf')
            for x in range(1, 2 * M + 1):
                if i + x > len(piles):
                    break
                sumval += piles[i + x - 1]
                best = max(best, sumval - dfs(i + x, max(M, x)))
            dp[(i, M)] = best
            return best
        total = sum(piles)
        return (total + dfs(0, 1)) // 2