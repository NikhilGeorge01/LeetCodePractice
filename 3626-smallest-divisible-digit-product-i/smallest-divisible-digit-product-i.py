class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digprod(num):
            prod = 1
            while num > 0:
                prod *= num%10
                num //= 10
            return prod
        while True:
            if digprod(n)%t == 0:
                break
            else:
                n += 1
        return n
        