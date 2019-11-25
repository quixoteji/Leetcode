#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t : return ''
        counter = collections.Counter(t)
        minLen, res = float('inf'), ''
        

# @lc code=end

