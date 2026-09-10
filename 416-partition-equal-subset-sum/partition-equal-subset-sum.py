class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        target = sum(nums)//2
        dp = [False for i in range(target+1)]
        dp[0] = True
        for i in range(len(nums)):
            temp = dp.copy()
            for j in range(target+1):
                if nums[i] <= j:
                    dp[j] = dp[j] or temp[j-nums[i]]
        return dp[-1] 