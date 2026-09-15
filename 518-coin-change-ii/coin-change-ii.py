class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[-1] = 1
        for i in range(len(coins)):
            temp = dp.copy()
            for j in range(len(dp) - 1, -1, -1):
                a = j + coins[i]
                if a >= len(dp):
                    a = 0
                else:
                    a = dp[j + coins[i]]
                dp[j] = a + temp[j]
        return dp[0]