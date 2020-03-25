#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([prices[i] - prices[i - 1] if prices[i] - prices[i - 1] > 0 else 0 for i in range(1, len(prices))])

        
# @lc code=end

