class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        else:
            return 2**n.bit_length()