#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        return self.sol1(start, end, bank)

    def sol1(self, start, end, bank) :
        queue = []
        queue.append(start)
        bank = set(bank)
        if end not in bank : return -1
        level = 0
        while queue : 
            l = len(queue)
            for i in range(l) :
                seq = queue.pop(0)
                for i in range(8) :
                    for char in ['A', 'C', 'G', 'T'] :
                        if seq[i] == char : continue
                        nseq = seq[:i] + char + seq[i + 1:]
                        if nseq == end : return level + 1
                        if nseq in bank : 
                            queue.append(nseq)
                            bank.remove(nseq)
            level += 1
        return -1
                      

        
# @lc code=end

