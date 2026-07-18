class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt = Counter(nums)
        cntG = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            c = 0
            for j in range(i, mx + 1, i):
                c += cnt[j]
                cntG[i] -= cntG[j]
            cntG[i] += c * (c - 1) // 2

        pref = list(accumulate(cntG))
        return [bisect_right(pref, q) for q in queries]