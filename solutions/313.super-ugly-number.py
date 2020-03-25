#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start

from heapq import heapify, heappop, heappush
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        super_ugly_numbers = []
        heap = [1]
        heapify(heap)
        indexes = {1 : [[0, p] for p in primes]}
        while len(super_ugly_numbers) < n :
            super_ugly_numbers.append(heappop(heap))
            for tup in indexes[super_ugly_numbers[-1]]:
                new_ugly = super_ugly_numbers[tup[0]] * tup[1]    
                if new_ugly in indexes:
                    indexes[new_ugly].append([tup[0] + 1, tup[1]])
                else:
                    indexes[new_ugly] = [[tup[0] + 1, tup[1]]]
                    heappush(heap, new_ugly)
            del indexes[super_ugly_numbers[-1]]
            
        return super_ugly_numbers[-1]
        
# @lc code=end

