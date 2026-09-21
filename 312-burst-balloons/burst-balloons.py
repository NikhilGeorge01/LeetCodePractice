class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        dp = {}
        nums = [1] + nums + [1]
        def dfs(i,j):
            if i == j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            mxs = 0
            for k in range(i,j):
                mxs = max(mxs, nums[i-1]*nums[k]*nums[j] + dfs(i,k) + dfs(k+1,j))
            dp[(i,j)] = mxs
            return mxs
        return dfs(1,len(nums) - 1)