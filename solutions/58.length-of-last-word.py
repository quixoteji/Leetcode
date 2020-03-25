#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if len(words) < 1 : return 0
        else : return len(words[-1])
        
# @lc code=end

