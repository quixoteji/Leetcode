class Solution:
    def canCompleteCircuit(self, gas, cost):
        return self.sol1(gas, cost)

    # Solution 1 :
    def sol1(self, gas, cost) :
        if len(gas) < 2 : return 0
        tank = 0
        for i in range(len(gas)) :
            tank = gas[i] - cost[i]
            idx = i + 1 
            while idx != i :
                if idx == len(gas) : idx = 0
                if tank < 0 : break
                else : tank += gas[idx] - cost[idx]
                idx = idx + 1 
            if tank >= 0 and idx == i : return idx        
        return -1
                

A = Solution()
print(A.canCompleteCircuit([3,1,1],[1,2,2]))


