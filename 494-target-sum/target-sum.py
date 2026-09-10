class Solution: 
    def findTargetSumWays(self, nums: List[int], target: int) -> int: 
        s = sum(nums) 
        dp = [0 for i in range(2*s + 3)] 

        if target > s or target < -s:
            return 0

        dp[s+1] = 1

        for i in range(len(nums)): 
            temp = dp.copy()
            dp = [0 for i in range(2*s + 3)]  

            for j in range(1, 2*s + 2): 
                if j-nums[i] >= 0:
                    dp[j] += temp[j-nums[i]]
                if j+nums[i] < len(dp):
                    dp[j] += temp[j+nums[i]]

        return dp[target+s+1]