class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(k):
            c = 0
            for i in piles:
                c += math.ceil(i/k)
            return c <= h
        high = max(piles)
        low = 1
        while low < high:
            mid = (high + low)//2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low
