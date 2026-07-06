class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        for l,r in intervals:
            if not stack:
                stack.append((l,r))
            else:
                sl,sr = stack[-1]
                if sl <= l and sr >= r:
                    continue
                else:
                    stack.append((l,r))
        return len(stack)