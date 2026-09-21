class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        l = len(p)
        check = Counter(p)
        dic = Counter(s[0:l])
        op = []
        print(check)
        for i in range(len(s) - l + 1):
            if dic == check:
                op.append(i)
            if i + l < len(s):
                dic[s[i]] -= 1
                dic[s[i+l]] += 1
        return op
