class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = set (nums)
        op = []
        for i in range(min(nums),max(nums)):
            if i not in a:
                op.append(i)
        return op