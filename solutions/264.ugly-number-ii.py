#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
from heapq import heappush, heappop, heapify
class Solution:
    def sol1(self, n) :
        seen = set()
        seen.add(1)
        nums, heap = [], []
        heappush(heap, 1)
        for i in range(n):
            temp = heappop(heap)
            nums.append(temp)
            for num in [2, 3, 5] :
                if num * temp not in seen :
                    seen.add(num * temp)
                    heappush(heap, num * temp)
        return nums[-1]

    def sol2(self, n) :
        i2 = i3 = i5 = 0
        nums = [1]
        for i in range(1, n):
            curr = [nums[i2] * 2, nums[i3] * 3, nums[i5] * 5]
            ugly = min(curr)
            nums.append(ugly)
            if nums[i2] * 2 == ugly: i2 += 1
            if nums[i3] * 3 == ugly: i3 += 1
            if nums[i5] * 5 == ugly: i5 += 1
        print(nums)
        return nums[-1]
            
# -10,-3,0,5,9

    def nthUglyNumber(self, n: int) -> int:
        return self.sol2(n)
        
# @lc code=end

