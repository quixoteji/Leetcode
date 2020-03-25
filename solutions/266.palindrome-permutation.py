#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#

# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = collections.Counter(s)
        ans = 0
        for val in count.values():
            if val % 2 != 0 : ans += 1
        return ans < 2
        
# @lc code=end

