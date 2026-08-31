class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minval = nums[0]
        minind = 0
        maxval = nums[0]
        maxind = 0
        for i in range(1,len(nums)):
            if nums[i] > maxval:
                maxval = nums[i]
                maxind = i
            if nums[i] < minval:
                minval = nums[i]
                minind = i
        a = len(nums) - (abs(minind - maxind)) + 1
        b = max(maxind,minind) + 1
        c =len(nums) - min(maxind, minind) 
        return min(a,b,c)
