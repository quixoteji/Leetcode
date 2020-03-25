#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        return self.sol1(nums1, nums2, k)


    def sol1(self, nums1, nums2, k) :
        nums = self.merge(nums1, nums2)
        print(nums)
        return self.cut(nums, k)

    def merge(self, nums1, nums2):
        ans = []
        while nums1 or nums2 :
            if nums1 > nums2 : ans.append(nums1.pop(0))
            else : ans.append(nums2.pop(0))
        return ans + nums1 + nums2

    def cut(self, nums, k) :
        pop = len(nums) - k
        stack = []
        for num in nums :
            if not stack or num <= stack[-1] : 
                stack.append(num)
            else :
                while num > stack[-1] and pop > 0 :
                    stack.pop()
                    pop -= 1
                stack.append(num)
        return stack


# @lc code=end

