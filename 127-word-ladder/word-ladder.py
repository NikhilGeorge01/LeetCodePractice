class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord,1)])
        def check(w1,w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        visited = set([beginWord])
        while q:
            wd,d = q.popleft()
            if wd == endWord:
                return d
            for a in wordList:
                if a not in visited and check(a,wd):
                    visited.add(a)
                    q.append((a,d+1))
        return 0