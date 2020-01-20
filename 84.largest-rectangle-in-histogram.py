#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.sol2(heights)

    # Solution 1 : brutal_force (time limit exceeded)
    def sol1(self, heights) :
        # if len(heights) == 1 : return heights[0]
        largest = 0
        for i in range(len(heights)) :
            for j in range(i, len(heights)) :
                area = (j - i + 1) * min(heights[i : j + 1])
                largest = largest if largest > area else area
        return largest

    # Solution 2 : 
    def sol2(self, heights) :
        stack = [-1]
        heights.append(0)
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]] :
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        
        return ans
        
# @lc code=end

