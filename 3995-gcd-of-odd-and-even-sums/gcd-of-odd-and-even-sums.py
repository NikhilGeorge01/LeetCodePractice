class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return (n * gcd(2+(n-1)*2, 4+(n-1)*2)) // 2