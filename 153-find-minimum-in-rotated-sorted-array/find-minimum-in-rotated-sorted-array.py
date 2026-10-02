class Solution:
    def findMin(self, nums: list[int]) -> int:
        high = len(nums) - 1
        low = 0
        while low < high:
            mid = (low+high)//2
            if nums[mid] >= nums[low] and nums[mid] <= nums[high]:
                return nums[low]
            if nums[mid] <= nums[high] and nums[mid] <= nums[low]:
                high = mid
            else:
                low = mid + 1
        return nums[low]
            