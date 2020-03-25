#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        counter = collections.Counter(candies)
        return len(counter) if len(counter) < len(candies)//2 else len(candies)//2
# @lc code=end

