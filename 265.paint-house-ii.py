#
# @lc app=leetcode id=265 lang=python3
#
# [265] Paint House II
#

# @lc code=start
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        return self.sol2(costs)

    def sol1(self, costs) :
        if not costs : return 0
        n, k = len(costs), len(costs[0])
        for i in range(1, n) :
            for j in range(k) :
                costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])
        return min(costs[-1])

    def sol2(self, costs) :
        if not costs : return 0
        n, k = len(costs), len(costs[0])
        for house in range(1, n) :
            minIdx = secIdx = None
            for color in range(k) :
                cost = costs[house - 1][color]
                if minIdx is None or cost < costs[house - 1][minIdx]:
                    secIdx = minIdx
                    minIdx = color
                elif secIdx is None or cost < costs[house - 1][secIdx]:
                    secIdx = color

            for color in range(k) :
                if color == minIdx : costs[house][color] += costs[house - 1][secIdx]
                else : costs[house][color] += costs[house - 1][minIdx]
        
        return min(costs[-1])
        
# @lc code=end

