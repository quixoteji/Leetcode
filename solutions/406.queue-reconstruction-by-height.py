#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        return self.sol1(people)

    # Solution 1 :
    def sol1(self, people) :
        people.sort(key=lambda x : x[0])
        
        
# @lc code=end

