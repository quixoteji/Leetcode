#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class FenwickTree :
    def __init__(self, n) :
        self.n = n + 1
        self.nums = [0 for _ in range(n + 1)]
        self.lowbits = lambda x : x & (-x)

    def update(self, i, val) :
        while i < self.n :
            self.nums[i] += val
            i += self.lowbits(i)

    def query(self, i) :
        ans = 0
        while i > 0 :
            ans += self.nums[i]
            i -= self.lowbits(i)
        return ans

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        curr = 1
        discrete = {}
        for n in sorted(set(nums)) :
            discrete[n], curr = curr, curr + 1

        fenwick = [0] * curr

        def add(i) :
            while i < len(fenwick) :
                fenwick[i] += 1
                i += i & -i
        def get_sum(i) : 
            ans = 0
            while i > 0 :
                ans += fenwick[i]
                i -= i & -i
            return ans

        ans = []
        for n in [discrete[i] for i in reversed(nums)] :
            ans.append(get_sum(n - 1))
            add(n)

        ans.reverse()

        return ans


        
        
# @lc code=end

