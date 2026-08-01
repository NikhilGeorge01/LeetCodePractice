class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(i,j):
            if i > j:
                return 0
            if i == j:
                return nums[i]
            return max(nums[i] - dfs(i+1,j) , nums[j] - dfs(i,j-1))
        return dfs(0,len(nums) - 1) >= 0