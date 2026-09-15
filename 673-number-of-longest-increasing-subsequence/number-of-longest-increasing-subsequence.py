class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1,1] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
        maxlen = max(dp[i][0] for i in range(len(dp)))

        ans = 0
        for i in range(len(dp)):
            if dp[i][0] == maxlen:
                ans += dp[i][1]

        return ans        