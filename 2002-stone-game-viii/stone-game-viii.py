class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        cumsum = [0]
        for x in stones:
            cumsum.append(cumsum[-1] + x)
        n = len(stones)
        dp = [0] * (n + 1)
        dp[n] = cumsum[n]
        for i in range(n - 1, 1, -1):
            dp[i] = max(cumsum[i] - dp[i + 1], dp[i + 1])
        return dp[2]