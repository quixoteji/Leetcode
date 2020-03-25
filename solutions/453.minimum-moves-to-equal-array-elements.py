#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
#
# algorithms
# Easy (49.63%)
# Likes:    427
# Dislikes: 647
# Total Accepted:    63.8K
# Total Submissions: 128.5K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty integer array of size n, find the minimum number of moves
# required to make all array elements equal, where a move is incrementing n - 1
# elements by 1.
# 
# Example:
# 
# Input:
# [1,2,3]
# 
# Output:
# 3
# 
# Explanation:
# Only three moves are needed (remember each move increments two elements):
# 
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 
# 
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        res = 0
        for i in range(1, len(nums)) :
            res += i * (nums[i - 1] - nums[i])
        return res
        
# @lc code=end

