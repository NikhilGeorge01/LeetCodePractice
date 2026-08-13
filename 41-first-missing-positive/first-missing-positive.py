class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = set(nums)
        for i in range(1,max(nums)):
            if i not in check:
                return i
        return max(1,max(nums) + 1)
