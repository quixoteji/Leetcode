from heapq import heappush, heappop, heapify
class Solution:
    def sol1(self, n) :
        heap = []
        nums = []
        heappush(heap, 1)
        for i in range(1, n) :
            temp = heappop(heap)
            while temp in nums : temp = heappop(heap)
            nums.append(temp)
            heappush(heap, temp * 2)
            heappush(heap, temp * 3)
            heappush(heap, temp * 5)
        return heappop(heap)
# -10,-3,0,5,9

A = Solution()
print(A.sol1(19))