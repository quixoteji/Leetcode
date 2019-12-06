#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return self.sol1(gas, cost)

    # Solution 1 :
    def sol1(self, gas, cost) :
        total, tank, start = 0, 0, 0
        for i in range(len(gas)) :
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0 :
                start = i + 1
                tank = 0
        return start if total < 0 else -1
        
# @lc code=end

