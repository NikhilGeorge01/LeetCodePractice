class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        class DS:
            def __init__(self,n):
                self.rank = [0]*n
                self.par = list(range(n))
            def find(self,x):
                if self.par[x] != x:
                    self.par[x] = self.find(self.par[x])
                return self.par[x]
            def union(self,x,y):
                px = self.find(x)
                py = self.find(y)
                if px == py:
                    return False
                if self.rank[px] < self.rank[py]:
                    self.par[px] = py
                elif self.rank[px] > self.rank[py]:
                    self.par[py] = px
                else:
                    self.par[py] = px
                    self.rank[px] += 1
                return True
        ds = DS(len(nums))
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] <= maxDiff:
                ds.union(i, i-1)
        op = []
        for a,b in queries:
            if ds.find(a) == ds.find(b):
                op.append(True)
            else:
                op.append(False)
        return op