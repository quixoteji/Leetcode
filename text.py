from heapq import heappush, heappop, heapify
class Solution:
    def sol2(self, n) :
        i2 = i3 = i5 = 0
        nums = [1]
        for i in range(n):
            curr = [nums[i2] * 2, nums[i3] * 3, nums[i5] * 5]
            ugly = min(curr)
            nums.append(ugly)
            if nums[i2] == ugly: i2 += 1
            if nums[i3] == ugly * 3: i3 += 1
            if nums[i5] == ugly * 5: i5 += 1
        print(nums)
        return nums[-1]
# -10,-3,0,5,9

A = Solution()
print(A.sol2(19))