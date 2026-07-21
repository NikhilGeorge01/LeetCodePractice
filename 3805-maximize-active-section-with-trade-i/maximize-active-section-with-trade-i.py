class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        seg = []
        o = 0
        for i in s:
            if i == '1':
                o += 1
            if not seg:
                seg.append([i,1])
            elif i == seg[-1][0]:
                seg[-1][1] += 1
            else:
                seg.append([i,1])
        delt = 0
        for i in range(1,len(seg)-1):
            if seg[i][0] == '1':
                delt = max(delt,seg[i-1][1] + seg[i+1][1])
        return delt + o
        
                 
                