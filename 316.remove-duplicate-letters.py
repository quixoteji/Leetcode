#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return self.sol1(s)

    def sol1(self, s) :
        stack = []
        seen = set()
        last_occurrence = {c : i for i, c in enumerate(s)}

        for i, c in enumerate(s) :
            if c not in seen :
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]] :
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
# @lc code=end

