class Solution:
    _graph = None
    _state = None
    _ans = []

    def dfs(self, node) : 
        if self._state[node] == 1 : return True
        if self._state[node] == 2 : return False
        self._state[node] = 1
        for nextNode in self._graph[node] :
            if self.dfs(nextNode) : return True
        self._state[node] = 2
        self._ans.insert(0, node)
    
    def findOrder(self, numCourses, prerequisites):
        self._graph = [list() for _ in range(numCourses)]
        self._state = [0] * numCourses
        for p in prerequisites :
            self._graph[p[1]].append(p[0])

        for node in range(numCourses):
            if self.dfs(node) : return []

        return self._ans 

A = Solution()

print(A.findOrder(1, []))


