from heapq import heappush, heappop, heapify
class Solution:
    def sol2(self, nums) :
        if not nums: return 0
        p, k = 1, 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] : 
                k += 1
                if k < 2 : p += 1
            else :
                k = 0
                nums[p] = nums[i]
                p += 1
        return p
# -10,-3,0,5,9

A = Solution()
print(A.sol2([0,0,1,1,1,1,2,3,3]))