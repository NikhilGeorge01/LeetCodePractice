class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = 0
        m2 = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > m2:
                m1 = m2
                m2 = nums[i]
            elif nums[i] > m1:
                m1 = nums[i]
        return (m1-1) * (m2-1)
                
