class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        c = 1
        btop = intervals[0][1]

        for a, b in intervals[1:]:
            if a < btop:
                if b < btop:
                    btop = b
            else:
                c += 1
                btop = b

        return len(intervals) - c