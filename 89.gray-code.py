#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return self.sol1(n)

    def sol1(self, n) :
        ans = []
        visited = set()
        self.dfs(ans, visited, 0, n)
        return ans

    def dfs(self, ans, visited, num, n) :
        if num in visited : return
        if num not in visited : 
            ans.append(num)
            visited.add(num)
        for i in range(n) :
            if num & (1 << i) == 0 :
                next = num | (1 << i)
            else :
                next = num & ~(1 << i)
            self.dfs(ans, visited, next, n)
        
        
# @lc code=end

