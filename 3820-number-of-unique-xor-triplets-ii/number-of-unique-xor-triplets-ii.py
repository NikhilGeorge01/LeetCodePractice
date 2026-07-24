class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s1 = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                s1.add(nums[i]^nums[j])
        res = set()
        for i in nums:
            for k in s1:
                res.add(i^k)
        return len(res)
