class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l,r = 0,0
        hm = {}
        maxl = 0
        while r < len(s):
            if s[r] in hm:
                hm[s[r]] += 1
            else:
                hm[s[r]] = 1
            r += 1
            while hm[s[r - 1]] > 2:
                hm[s[l]] -= 1
                l += 1
            maxl = max(maxl, r - l)
        return maxl