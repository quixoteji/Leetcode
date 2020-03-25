#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s : return s
        strs = s.strip().split()[::-1]
        return ' '.join(strs)

        
# @lc code=end

