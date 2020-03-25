#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        counter = collections.Counter(nums)
        for num in counter :
            if (k > 0 and num + k in counter) or (k == 0 and counter[num] > 1) :
                res += 1
        return res
# @lc code=end

