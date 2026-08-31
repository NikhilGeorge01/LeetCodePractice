class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp = head
        prev = temp
        cur = temp.next
        cps = []
        ind = 1
        while cur.next:
            if (cur.val > cur.next.val and cur.val > prev.val) or (cur.val < cur.next.val and cur.val < prev.val):
                cps.append(ind)
            ind += 1
            prev = cur
            cur = cur.next
        print(cps)
        if len(cps) < 2:
            return [-1, -1]
        else:
            minval = float('inf')
            for i in range(1, len(cps)):
                if cps[i] - cps[i-1] < minval:
                    minval = cps[i] - cps[i-1]
            return [minval, cps[-1] - cps[0]]