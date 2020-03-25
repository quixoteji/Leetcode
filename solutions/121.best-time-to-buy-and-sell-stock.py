#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def brute_force(self, prices) :
        profit = 0
        for i in range(len(prices)) :
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i] :
                    profit = max(profit, prices[j] - prices[i])
        return profit

    def one_run(self, prices) :
        minprice = float('inf')
        maxprofit = 0
        for price in prices :
            if price < minprice : minprice = price
            elif price > minprice : maxprofit = max(price - minprice, maxprofit)
        return maxprofit

    def dp1(self, prices) :
        if not prices: return 0
        minprice = [prices[0] for i in range(len(prices))]
        profit = [0 for i in range(len(prices))]
        for i in range(len(prices)) :
            if i > 0 :
                minprice[i] = min(minprice[i - 1], prices[i])
                profit[i] = max(profit[i - 1], prices[i] - minprice[i])
        return profit[-1]

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2 : return 0

        profit = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        maxprofit = [profit[0] for i in range(len(profit))]
        for i in range(1, len(profit)) :
            if maxprofit[i - 1] > 0 :
                maxprofit[i] = maxprofit[i - 1] + profit[i]
            else :
                maxprofit[i] = profit[i]
        return max(maxprofit) if max(maxprofit) > 0 else 0

        
# @lc code=end

