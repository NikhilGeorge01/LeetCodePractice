class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        a = nums[0]
        b = nums[-1]
        if k == len(nums):
            return max(nums)
        if k == 1:
            for x in sorted(nums, reverse=True):
                if nums.count(x) == 1:
                    return x
            return -1
        if a > b:
            a,b = b,a
        abool = True
        bbool = True
        for i in range(1,len(nums) - 1):
            if nums[i] == a:
                abool = False
            if nums[i] == b:
                bbool = False
        if a == b:
            return -1 
        if abool and bbool:
            return b
        elif abool:
            return a
        elif bbool:
            return b
        return -1