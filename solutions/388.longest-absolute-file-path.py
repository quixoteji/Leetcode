#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        return self.sol1(input)

    def sol1(self, input) :
        stack, rst, arr = [], 0, input.split('\n')
        for i in arr :
            level = i.count('\t')
            while len(stack) > level : stack.pop()
            stack.append(i[level:])
            if '.' in i : rst = max(rst, len('/'.join(stack)))
        return rst

        
# @lc code=end

