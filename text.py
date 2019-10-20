class Solution:
    def findMedianSortedArrays(self, nums1, nums2) :
        # k = (l1 + l2) / 2
        # m1 in l1 and m2 in l2
        # right median : (l1+l2+1)//2
        # left median : (l1+l2-1)//2
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2 : return self.findMedianSortedArrays(nums2, nums1)
        k = (l1 + l2 + 1) // 2
        l, r = 0, l1 - 1
        while l < r :
            m1 = l + (r - l) // 2 
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1] : l = m1 + 1
            else : r = m1
        m1, m2 = l, k - l
        if m1 < 0 : c1, c2 = nums2[m2], nums2[m2 - 1]
        if m2 < 0 : c1, c2 = nums1[m1], nums1[m1 - 1]
        c1, c2 = min(nums1[m1], nums2[m2]), max(nums1[m1 - 1], nums2[m2 - 1])
        if (l1 + l2) % 2 == 0 : 
            return (c1 + c2) / 2
        else : 
            return c1  

A = Solution()
print(A.findMedianSortedArrays([1,3], [2]))