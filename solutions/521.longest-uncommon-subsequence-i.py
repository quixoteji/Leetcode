#
# @lc app=leetcode id=521 lang=python3
#
# [521] Longest Uncommon Subsequence I 
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:

        return max(len(a), len(b)) if a !=b else -1
        
# @lc code=end

