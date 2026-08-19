class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        total = 2 * n
        rows = {}
        for a,b in reservedSeats:
            if a not in rows:
                rows[a] = set()
            rows[a].add(b)
        for seats in rows.values():
            block1 = any(x in seats for x in [2,3,4,5])
            block2 = any(x in seats for x in [4,5,6,7])
            block3 = any(x in seats for x in [6,7,8,9])
            if block1 and block2 and block3:
                total -= 2
            elif block1 and block3:
                total -= 1
            elif block1 or block2 or block3:
                total -= 1
        return total