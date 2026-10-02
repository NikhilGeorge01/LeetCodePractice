class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        s = []
        n = len(digits)
        res = []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv','9':'wxyz'}
        def backtrack(i):
            if i == n:
                res.append(''.join(s))
                return
            for j in dic[digits[i]]:
                s.append(j)
                backtrack(i+1)
                s.pop()  
        backtrack(0)
        return res          
