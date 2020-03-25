#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#

# @lc code=start
class Solution:
    def reverse(self, s, left, right):
        while left < right :
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0 , len(s) - 1)
        left = 0
        for i in range(len(s)) :
            if s[i] == ' ' :
                self.reverse(s, left, i - 1)
                left = i + 1
            if i == len(s) - 1 :
                self.reverse(s, left, i)
        
        
# @lc code=end

