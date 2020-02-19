#
# @lc app=leetcode id=358 lang=python3
#
# [358] Rearrange String k Distance Apart
#

# @lc code=start
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        return self.sol1(s, k)

    def sol1(self, s, k) :
        heap = [(-freq, char) for char, freq in collections.Counter(str).items()]

        heapq.heapify(heap)
        res = []
        while len(res) < len(str) :
            if not heap : return ''
            freq, char = heapq.heappop(heap)
            stack = []
            res.append(char)
            for j in range(k - 1) : 
                if len(res) == len(str): return "".join(res)
                if not heap: return ""
                fre, nex = heapq.heappop(heap)
                res.append(nex)
                if fre < -1: 
                    stack.append((fre+1, nex))
            while stack:
                heapq.heappush(heap, stack.pop())
            heapq.heappush(heap, (freq+1, char))
        return "".join(res)

        
# @lc code=end

