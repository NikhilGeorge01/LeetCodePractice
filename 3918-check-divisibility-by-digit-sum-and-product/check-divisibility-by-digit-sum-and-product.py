class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sval = 0
        pval = 1
        t = n
        while t > 0:
            pval *= t%10
            sval += t%10
            t = t//10
        return n%(sval + pval) == 0 