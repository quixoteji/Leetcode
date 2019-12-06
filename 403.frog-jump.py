#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        return self.sol2(stones)

    # Solution 1 : dfs (time limit exceeded)
    def sol1(self, stones) :
        if stones[0] != 0 or stones[1] != 1 : return False
        if len(stones) == 2 : return True
        pos, step = 1, 1
        return self.dfs(pos, step, stones[2:])

    def dfs(self, pos, step, stones) :
        if pos + step <= pos : return False
        if pos > stones[-1] : return False
        if pos == stones[-1] : return True
        steps = [step - 1, step, step + 1]
        for s in steps :
            if pos + s in stones and self.dfs(pos + s, s, stones):
                return True
        return False

    # Solution 2 : iteration
    def sol2(self, stones) :
        return self.ddfs(stones, 0, 0)
    def ddfs(self, stones, pos, k) :
        for i in range(pos + 1, len(stones)):
            gap = stones[i] - stones[pos]
            if gap < k - 1 : continue
            
        

    
        
# @lc code=end

