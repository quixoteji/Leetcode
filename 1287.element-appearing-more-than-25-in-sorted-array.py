#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return self.sol1(arr)

    def sol1(self, arr) :
        counter = collections.Counter(arr)
        for c in counter :
            if counter[c] > 0.25 * len(arr) :
                return c
        
# @lc code=end

