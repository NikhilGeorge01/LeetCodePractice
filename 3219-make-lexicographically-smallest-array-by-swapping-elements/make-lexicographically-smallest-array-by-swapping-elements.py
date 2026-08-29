class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs = sorted((x, i) for i, x in enumerate(nums))
        res = nums[:]
        i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and pairs[j + 1][0] - pairs[j][0] <= limit:
                j += 1
            indices = sorted(pairs[k][1] for k in range(i, j + 1))
            values = [pairs[k][0] for k in range(i, j + 1)]
            for idx, val in zip(indices, values):
                res[idx] = val
            i = j + 1
        return res