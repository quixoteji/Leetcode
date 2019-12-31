#
# @lc app=leetcode id=339 lang=python3
#
# [339] Nested List Weight Sum
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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.sol3(nestedList)

    # Solution 1 : dfs
    def sol1(self, nestedList) :
        return self.dfs(nestedList, 1)

    def dfs(self, nestedList, level) :
        sum = 0
        for n in nestedList :
            if n.isInteger() : sum += n.getInteger() * level
            else : sum += self.dfs(n.getList(), level + 1)
        return sum

    # Solution 2 : bfs
    def sol2(self, nestedList) :
        stack = []
        level = 1
        ans = 0
        stack.append(nestedList)
        while stack :
            print('level : ' + str(level))
            l = len(stack)
            for i in range(l) :
                nl = stack.pop()
                for n in nl :
                    if n.isInteger() : 
                        print(n.getInteger())
                        ans += level * n.getInteger()
                    else : stack.append(n.getList())
            level += 1
        return ans

    # # Solution 3 : 
    # [[[[55]]],[[31]],[99],[],75]
    def sol3(self, nestedList) :
        if not nestedList:
            return 0
        depth = 1
        res = sum([x.getInteger() for x in nestedList if x.isInteger()])*depth
        nestedList = [l for x in nestedList for l in x.getList() if not x.isInteger()]
        while nestedList:
            depth += 1
            res += sum([x.getInteger() for x in nestedList if x.isInteger()])*depth
            nestedList = [l for x in nestedList for l in x.getList() if not x.isInteger()]
        return res
# @lc code=end

