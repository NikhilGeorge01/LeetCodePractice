class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m = len(word2)
        n = len(word1)
        last = [-1 for _ in range(len(word2))]
        j = m - 1
        for i in range(n -1, -1, -1):
            if j < 0:
                break
            if word2[j] == word1[i]:
                last[j] = i
                j -= 1
        change = False
        j = 0
        op = []
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                op.append(i)
                j += 1
            elif not change and (j == m-1 or last[j+1] > i):
                change = True
                op.append(i)
                j += 1
        return op if len(op) == m else []