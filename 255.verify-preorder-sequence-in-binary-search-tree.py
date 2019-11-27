#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#

# @lc code=start
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = [float('inf')]
        minVal = float('inf')
        for val in preorder :
            if val < minVal : return False
            while val > stack[-1] : minVal = stack.pop()
            stack.append(val)
        return True
        
# @lc code=end

