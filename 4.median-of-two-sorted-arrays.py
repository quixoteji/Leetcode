#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:

    def sol1(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 + l2) % 2 == 1 : c = (l1 + l2 + 1) / 2
        else : 

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.sol1(nums1, nums2)

        # l1, l2 = len(nums1), len(nums2)
        # if l1 > l2 : return self.findMedianSortedArrays(nums2, nums1)
        # k = (l1 + l2 + 1) // 2
        # l, r = 0, l1 - 1
        # while l < r :
        #     m1 = l + (r - l) // 2 
        #     m2 = k - m1
        #     if nums1[m1] < nums2[m2 - 1] : l = m1 + 1
        #     else : r = m1
        # m1, m2 = l, k - l
        # if m1 <= 0 : c1, c2 = nums2[m2], nums2[m2 - 1]
        # if m2 <= 0 : c1, c2 = nums1[m1], nums1[m1 - 1]
        # c1, c2 = min(nums1[m1], num2[m2]), max(nums1[m1 - 1], nums2[m2 - 1])
        # if (l1 + l2) % 2 == 0 : 
        #     return (c1 + c2) / 2
        # else : 
        #     return c1  


        

# @lc code=end

