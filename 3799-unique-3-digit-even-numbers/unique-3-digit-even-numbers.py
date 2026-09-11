class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c = Counter(digits)
        ans = 0
        for i in range(1, 10):          
            if c[i] == 0:
                continue
            c[i] -= 1
            for j in range(10):         
                if c[j] == 0:
                    continue
                c[j] -= 1
                for k in range(0, 10, 2):   
                    if c[k] > 0:
                        ans += 1
                c[j] += 1
            c[i] += 1
        return ans