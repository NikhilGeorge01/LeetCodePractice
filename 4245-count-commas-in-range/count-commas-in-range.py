class Solution:
    def countCommas(self, n: int) -> int:
        c = 0
        for i in range(n+1):
            if i // 1000 > 0:
                c += 1
        return c