class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        ones = 0
        res = ''
        for r in range(len(s)):
            if s[r] == '1':
                ones += 1
            while ones == k:
                cur = s[l:r + 1]
                if not res or len(cur) < len(res) or len(cur) == len(res) and cur < res:
                    res = cur
                if s[l] == '1':
                    ones -= 1
                l += 1
        return res