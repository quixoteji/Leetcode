#
# @lc app=leetcode id=444 lang=python3
#
# [444] Sequence Reconstruction
#

# @lc code=start
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        return self.sol2(org, seqs)

    # Solution 1 : topological sort
    def sol1(self, org, seqs) :
        if not seqs or not any(seqs): return False
        # map construction
        graph = [list() for _ in range(len(org) + 1)]
        for seq in seqs :
            for i in range(len(seq) - 1):
                graph[seq[i]].append(seq[i + 1])
        # dfs
        visited = set()
        visited.add(0)
        for n in org :
            visited.add(n)
            if self.dfs(graph, visited, n) : return True
            visited.remove(n)
        return False

    def dfs(self, graph, visited, n) :
        # print(n)
        # print(graph[n])
        if not graph[n] : return len(visited) == len(graph)
        
        for node in graph[n] :
            visited.add(node)
            if self.dfs(graph, visited, node) : return True
            visited.remove(node)

    # Solution2 : topological sort
    def sol2(self, org, seqs) :
        children = collections.defaultdict(set)
        parents = collections.defaultdict(set)
        nodes = set()
        for seq in seqs :
            for i in range(len(seq)):
                nodes.add(seq[i])
                if i > 0 : parents[seq[i]].add(seq[i-1])
                if i < len(seq) - 1 : children[seq[i]].add(seq[i+1])

        potential_parents = [n for n in nodes if not parents[n]]
        ans = []
        count = len(potential_parents)

        while count == 1 :
            cur_parent, count = potential_parents.pop(), count - 1
            ans.append(cur_parent)
            nodes.remove(cur_parent)
            for n in children[cur_parent] :
                parents[n].remove(cur_parent)
                if not parents[n] :
                    potential_parents.append(n)
                    count += 1
        return True if not nodes and ans == org else False

# @lc code=end

