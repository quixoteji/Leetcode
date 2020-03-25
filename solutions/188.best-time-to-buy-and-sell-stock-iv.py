#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0 :  return 0
        n = len(prices)
        _global = [0 for _ in range(k + 1)]
        _local = [0 for _ in range(k + 1)]
        for i in range(1, n) :
            diff = prices[i] - prices[i - 1]
            for j in range(1, k + 1) :
                _local[i][j] = max(_global[i - 1][j - 1] + max(0, diff), _local[i - 1][j] + diff)
                _global[i][j] = max(_global[i - 1][j], _local[i - 1][j])
        print(_global)
        return _global[-1][-1]        
# @lc code=end

