#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        h_index = 0
        for i in range(n) :
            if citations[i] > i : h_index += 1
            else : break
        return h_index

        
# @lc code=end

