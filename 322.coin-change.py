#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.sol1(coins, amount)

    # Solution1 : dfs
    def sol1(self, coins, amount) :
        coins.sort(reverse=True)
        ans = amount + 1
        self.dfs(ans, coins, amount, 0, 0)
        return -1 if ans == amount + 1 else ans

    def dfs(self, ans, coins, amount, idx, curr) :
        if amount == 0 :
            ans = min(ans, curr)
            return
        if idx == len(coins) : return
        for i, coin in enumerate(coins) :
            self.dfs(ans, coins, amount-coin, i, curr + 1)
        
    # Solution 2 : dp
    def 
        
        
# @lc code=end

