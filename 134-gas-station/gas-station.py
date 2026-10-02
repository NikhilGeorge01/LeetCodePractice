class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        tot = sum(gas) - sum(cost)
        if tot < 0:
            return -1
        tot = 0
        ind = 0
        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            if tot < 0:
                tot = 0
                ind = i + 1
        return ind
                
        