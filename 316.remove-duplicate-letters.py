#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return self.sol1(s)

    def sol1(self, s) :
        t = list(s[::-1])
        hashset = set()
        for char in t :
            if char in hashset : char = ''
            hashset.add(char)
        print(t[::-1])
        return ''.join(t[::-1])
# @lc code=end

