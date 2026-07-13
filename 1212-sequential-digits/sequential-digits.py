class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        op = []
        def fun(start):
            if start > high:
                return
            if low <= start and high >= start:
                op.append(start)
            if start%10 == 9:
                return
            new = start*10 + (start%10 + 1)
            return fun(new) 
        for i in range(1,10):
            fun(i)
        return sorted(op)