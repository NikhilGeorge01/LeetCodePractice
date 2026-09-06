class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pmax = []
        smin = [0] * len(nums)
        for i in range(len(nums)):
            if not pmax:
                pmax.append(nums[i])
            else:
                pmax.append(max(pmax[-1], nums[i]))
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                smin[i] = nums[i]
            else:
                smin[i] = min(smin[i + 1], nums[i])
        for i in range(len(nums)):
            if pmax[i] - smin[i] <= k:
                return i
        return -1