#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    _graph = None
    _state = None

    def dfs(self, i) :
        if self._state[i] == 1 : return True
        if self._state[i] == 2 : return False
        self._state[i] = 1
        for neighbor in self._graph[i] :
            if self.dfs(neighbor) : return True
        self._state[i] = 2
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self._graph = [list() for _ in range(numCourses)]
        # state : 0 == unknown, 1 == visiting, 2 == visited
        self._state = [0] * numCourses
        for p in prerequisites :
            self._graph[p[0]].append(p[1])
        for i in range(numCourses):
            if self.dfs(i) : return False
        return True
        
        
# @lc code=end

