class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [0] * len(gas)
        for i in range(len(gas)):
            net[i] = gas[i] - cost[i]
        summ = 0
        for e in net:
            summ += e
        if summ < 0: return -1
        for begin in range(len(net)):
            summ = 0
            cut = net[begin:] + net[:begin]
            for e in cut:
                summ += e
                if summ < 0:
                    break
            if summ >= 0:
                return begin
        return -1