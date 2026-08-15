class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if max(nums) == 0:
            return 0
        op = 0
        for i in nums:
            op = op ^i
        if op == 0:
            return len(nums) - 1
        else:
            return len(nums)