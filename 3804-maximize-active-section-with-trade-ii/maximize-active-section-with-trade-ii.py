from dataclasses import dataclass
from itertools import pairwise

@dataclass
class Group:
    start: int
    length: int

class SparseTable:
    def __init__(self, nums):
        n = len(nums)
        self.st = [nums[:]]
        k = 1
        while (1 << k) <= n:
            prev = self.st[-1]
            cur = [0] * (n - (1 << k) + 1)
            for i in range(len(cur)):
                cur[i] = max(prev[i], prev[i + (1 << (k - 1))])
            self.st.append(cur)
            k += 1

    def query(self, l, r):
        k = (r - l + 1).bit_length() - 1
        return max(self.st[k][l], self.st[k][r - (1 << k) + 1])

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count("1")
        groups = []
        idx = []
        for i, c in enumerate(s):
            if c == "0":
                if i and s[i - 1] == "0":
                    groups[-1].length += 1
                else:
                    groups.append(Group(i, 1))
            idx.append(len(groups) - 1)

        if not groups:
            return [ones] * len(queries)

        merge = [a.length + b.length for a, b in pairwise(groups)]
        st = SparseTable(merge)

        ans = []

        for l, r in queries:
            res = ones

            left = -1 if idx[l] == -1 else groups[idx[l]].length - (l - groups[idx[l]].start)
            right = -1 if idx[r] == -1 else r - groups[idx[r]].start + 1

            if s[l] == "0" and s[r] == "0" and idx[l] + 1 == idx[r]:
                res = max(res, ones + left + right)

            L = idx[l] + 1
            R = idx[r] if s[r] == "1" else idx[r] - 1
            if L <= R - 1:
                res = max(res, ones + st.query(L, R - 1))

            if s[l] == "0" and idx[l] + 1 <= (idx[r] if s[r] == "1" else idx[r] - 1):
                res = max(res, ones + left + groups[idx[l] + 1].length)

            if s[r] == "0" and idx[l] < idx[r] - 1:
                res = max(res, ones + right + groups[idx[r] - 1].length)

            ans.append(res)

        return ans