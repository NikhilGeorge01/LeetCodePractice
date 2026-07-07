class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        zc = 0
        x = []
        sm = 0
        for i in str(n):
            if i == '0':
                continue
            else:
                x.append(i)
                sm += int(i)
        return int(''.join(x)) * sm