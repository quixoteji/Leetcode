#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#

# @lc code=start
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        return self.sol1(preorder)
    
    def sol1(self, preorder) :
        stack = []
        lower = -1 << 31
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True
        
# @lc code=end

