#
# @lc app=leetcode id=385 lang=python3
#
# [385] Mini Parser
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        try: return NestedInteger(int(s))
        except: pass
		
        stack = [NestedInteger()]
        num = list(map(int, (x for x in re.split('[\[\],]', s) if x)))
        
        for i, x in enumerate(s):
            if x=='[':
                temp = NestedInteger()
                stack[-1].add(temp)
                stack.append(temp)
            elif x==']':
                if s[i-1].isdigit(): stack[-1].add(NestedInteger(num.pop(0)))
                stack.pop()
            elif x==',':
                if s[i-1].isdigit(): stack[-1].add(NestedInteger(num.pop(0)))
        return stack[0].getList()[0]
# @lc code=end

  