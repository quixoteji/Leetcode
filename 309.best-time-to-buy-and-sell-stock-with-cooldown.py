#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.sol1(prices)

    def sol1(self, prices) :
        if not prices: return 0
        sell = [0 for _ in prices]
        buy = [0 for _ in prices]
        sell[0] = 0
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], (sell[i - 2] if i > 1 else 0) - prices[i])
        return sell[-1]


# @lc code=end

