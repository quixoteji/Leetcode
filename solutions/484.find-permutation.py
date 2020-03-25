#
# @lc app=leetcode id=484 lang=python3
#
# [484] Find Permutation
#

# @lc code=start
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        return self.sol1(s)

    def sol1(self, s) :
        ans = []
        stack = []
        for i in range(1, len(s) + 1) :
            if s[i - 1] == 'I' :
                stack.append(i)
                while stack :
                    ans.append(stack.pop())
            else :
                stack.append(i)
        stack.append(len(s) + 1)
        while stack :
            ans.append(stack.pop())
        return ans



        
# @lc code=end

