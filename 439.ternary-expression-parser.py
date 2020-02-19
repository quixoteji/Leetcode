#
# @lc app=leetcode id=439 lang=python3
#
# [439] Ternary Expression Parser
#

# @lc code=start
class Solution:
    def parseTernary(self, expression: str) -> str:
        return self.parse(expression)

    def parse(self, expression) :
        def dfs(it):
            first, second = next(it), next(it, None)
        
            if not second or second == ':':
                return first
            else:
                T, F = dfs(it), dfs(it)
                return T if first == 'T' else F

        return dfs(iter(expression))

        
# @lc code=end

