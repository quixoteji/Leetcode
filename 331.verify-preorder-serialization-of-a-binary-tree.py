#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        return self.solution1(preorder)

    def solution1(self, preorder) :
        slots = 1
        
        prev = None  # previous character
        for ch in preorder:
            if ch == ',':
                # one node takes one slot
                slots -= 1

                # no more slots available
                if slots < 0:
                    return False

                # non-empty node creates two children slots
                if prev != '#':
                    slots += 2
            prev = ch
        
        # the last node
        slots = slots + 1 if ch != '#' else slots - 1 
        # all slots should be used up
        return slots == 0


        
# @lc code=end

