#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float('-inf')
        for i in range(len(prices)) :
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return 0 if profit < 0 else profit

        
# @lc code=end

