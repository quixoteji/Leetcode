#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self._sum = [sum(nums[:i + 1]) for i in range(len(nums))]
        

    def sumRange(self, i: int, j: int) -> int:
        if i == 0 : return self._sum[j]
        return self._sum[j] - self._sum[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

