#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        return self.dp1(stones)

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

    # Solution 2 : dp bottom up
    def dp1(self, stones) :
        hashtable = collections.defaultdict(set)
        hashtable[0].add(0)
        for i in range(len(stones)):
            if stones[i] in hashtable :
                for val in hashtable[stones[i]] :
                    if val > 0 : hashtable[stones[i]+val].add(val)
                    if val > 1 : hashtable[stones[i]+val-1].add(val-1)
                    hashtable[stones[i]+val+1].add(val+1)
        return stones[-1] in hashtable


    
            
        

    
        
# @lc code=end

