class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        temp = []
        csum = 0
        candidates.sort()
        n = len(candidates)
        def backtrack(i): 
            nonlocal csum
            if csum == target:
                res.append(temp.copy())
                return
            for j in range(i,n):
                if candidates[j] + csum > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                csum += candidates[j]
                temp.append(candidates[j])
                backtrack(j+1)
                csum -= candidates[j]
                temp.pop()
        backtrack(0)
        return res
                
             