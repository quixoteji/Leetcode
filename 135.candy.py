#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        return self.sol1(ratings)

    def sol1(self, ratings) :
        l2r = [1 for _ in ratings]
        r2l = [1 for _ in ratings]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] : l2r[i] = l2r[i - 1] + 1
        for i in reversed(range(len(ratings) - 1)):
            if ratings[i] > ratings[i + 1] : r2l[i] = r2l[i + 1] + 1
            
        return sum([max(l2r[i], r2l[i]) for i in range(len(ratings))])        
# @lc code=end

