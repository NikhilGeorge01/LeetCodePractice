class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        chk = set(nums)
        temp = k
        while True:
            if temp not in chk:
                return temp
            else:
                temp += k

            