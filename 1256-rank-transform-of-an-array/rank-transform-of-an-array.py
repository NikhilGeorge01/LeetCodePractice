class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        newarr = [(arr[i], i) for i in range(len(arr))]
        newarr.sort()
        ans = [0] * len(arr)
        rank = 1
        prev = None
        for a, b in newarr:
            if a != prev:
                prev = a
                ans[b] = rank
                rank += 1
            else:
                ans[b] = rank - 1
        return ans