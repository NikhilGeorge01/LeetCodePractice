class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        def backtrack(st):
            if len(st) == len(target):
                return st if st > target else ""
            c = target[len(st)]
            if freq[c]:
                freq[c] -= 1
                if self.can_greater(freq, target[len(st) + 1:]):
                    res = backtrack(st + c)
                    if res:
                        return res
                freq[c] += 1
            for c in range(ord(target[len(st)]) + 1, ord("z") + 1):
                c = chr(c)
                if freq[c]:
                    freq[c] -= 1
                    return st + c + "".join(c * freq[c] for c in sorted(freq))
            return ""
        return backtrack("")
    def can_greater(self, freq, target):
        mx = "".join(c * freq[c] for c in sorted(freq, reverse=True))
        return mx > target