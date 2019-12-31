#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        return self.sol1(n, edges)

    # Solution 1 : BFS
    def sol1(self, n, edges) :
        if n <= 1 : return [0]
        degrees = [0] * n
        graph = {x : [] for x in range(n)}
        for edge in edges :
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        queue = [x for x in range(n) if degrees[x] == 1]
        res = []
        while queue :
            temp = []
            res = queue[:]
            for x1 in queue :
                for x2 in graph[x1] :
                    degrees[x2] -= 1
                    if degrees[x2] == 1 :
                        temp.append(x2)
            queue = temp
        return res




        
# @lc code=end

