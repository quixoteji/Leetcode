#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        set1, set2 = set(nums1), set(nums2)
        for num in set1 : 
            if num in set2 : ans.append(num)
        return ans
# @lc code=end

