#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.sol3(nums1, nums2)

    def sol1(self, nums1, nums2) : 
        ans = [-1 for _ in nums1]
        for i in range(len(nums1)) :
            found = False
            for j in range(len(nums2)) :
                if nums2[j] == nums1[i] : found = True
                elif found and nums2[j] > nums1[i] :
                    ans[i] = nums2[j]
                    break
                else : continue
        return ans
    
    def sol2(self, nums1, nums2) :
        ans = [-1 for _ in nums1]
        hashmap = dict()
        for i, num in enumerate(nums2) : hashmap[num] = i
        for i in range(len(nums1)) :
            for j in range(hashmap[nums1[i]], len(nums2)) :
                if nums2[j] > nums1[i] : 
                    ans[i] = nums2[j]
                    break
        return ans

    def sol3(self, nums1, nums2) :
        # momentum stack
        stack = []
        # num : next great
        hashmap = dict()
        for num in nums2 :
            while stack and num > stack[-1] :
                hashmap[stack.pop()] = num
            stack.append(num)
        while stack :
            hashmap[stack.pop()] = -1
        res = []
        for num in nums1 :
            res.append(hashmap[num])
        return res

    
# @lc code=end

