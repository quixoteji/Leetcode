#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def dfs(self, node, state, graph, ans) : 
        if state[node] == 1 : return True
        if state[node] == 2 : return False
        state[node] = 1
        for nextNode in graph[node] :
            if self.dfs(nextNode, state, graph, ans) : return True
        state[node] = 2
        ans.insert(0, node)
        return False
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [list() for _ in range(numCourses)]
        state = [0] * numCourses
        ans = []
        for p in prerequisites :
            graph[p[1]].append(p[0])

        for node in range(numCourses):
            if self.dfs(node, state, graph, ans) : return []

        return ans
        
# @lc code=end

