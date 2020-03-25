#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        l = sorted(counter)[::-1]
        return l[2] if len(l) > 2 else l[0]

        
# @lc code=end

