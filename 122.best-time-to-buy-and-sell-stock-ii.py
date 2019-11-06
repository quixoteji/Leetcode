#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf')
        for price in prices:
            if price < minprice : minprice = price
            if price > minprice : 
                profit += price - minprice
                minprice = float('inf')
        return profit

        
# @lc code=end

