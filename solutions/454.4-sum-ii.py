#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        return self.sol2(A, B, C, D)
    # solution 1 : brutal force
    def sol1(self, A, B, C, D) :
        ans = 0
        for a in A :
            for b in B :
                for c in C :
                    for d in D :
                        if a + b + c + d == 0 :
                            ans += 1
        return ans
        
    # solution 2 : hashmap
    def sol2(self, A, B, C, D) :
        ans = 0
        hashmap = collections.defaultdict(int)
        for a in A :
            for b in B :
                hashmap[0 - a - b] += 1
        for c in C :
            for d in D :
                if c + d in hashmap : ans += hashmap[c + d]
        return ans
# @lc code=end

