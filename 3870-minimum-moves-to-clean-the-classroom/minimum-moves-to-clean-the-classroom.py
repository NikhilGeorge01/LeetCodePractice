class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}
        si = sj = 0
        k = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1
                elif classroom[i][j] == 'S':
                    si, sj = i, j
        full = (1 << k) - 1
        q = deque([(si, sj, energy, 0, 0)])
        best = {(si, sj, 0): energy}
        while q:
            i, j, e, mask, moves = q.popleft()
            if mask == full:
                return moves
            if e == 0:
                continue
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and classroom[ni][nj] != 'X':
                    ne = e - 1
                    nmask = mask
                    if (ni, nj) in litter:
                        nmask |= 1 << litter[(ni, nj)]
                    if classroom[ni][nj] == 'R':
                        ne = energy
                    state = (ni, nj, nmask)
                    if best.get(state, -1) >= ne:
                        continue
                    best[state] = ne
                    q.append((ni, nj, ne, nmask, moves + 1))
        return -1