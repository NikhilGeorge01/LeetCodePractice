class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = []
        rn = int(n**0.5)
        for i in range(1,rn+1):
            squares.append(i*i)
        @cache
        def fun(x):
            if x <= 0:
                return False
            for sq in squares:
                if sq > x:
                    break
                if not fun(x - sq):
                    return True
            return False
        return fun(n) 