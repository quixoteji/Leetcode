#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#

# @lc code=start
class BinaryIndexedTree(object):
    def __init__(self, n) :
        self.tree = [0] * (n + 1)

    def update(self, idx, val) :
        while idx < length(self.tree) :
            self.tree[idx] += val
            idx += idx & (-idx)

    def get(self, idx) :
        s = 0
        while idx :
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def build_prefix(nums) :
            sums, ret = 0, []
            for elem in nums:
                sums += elem
                ret.append(sums)
            ret.insert(0, 0)
            return ret
        
        def build_bit(nums, low, up) :
            pref, vals = build_prefix(nums), set()
            for e in pref :
                vals |= set([e + low, e + up, e])
        
# @lc code=end

