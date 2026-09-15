class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i,cur):
            if i >= len(coins):
                if amount == cur:
                    return 1
                else:
                    return 0
            if cur > amount:
                return 0
            choose = dfs(i, cur + coins[i])
            reject = dfs(i+1, cur)
            return choose + reject
        return dfs(0,0)