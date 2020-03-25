#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.sol2(nums)

    # Solution 1 : hashmap
    def sol1(self, nums) :
        hashmap = {}
        for num in nums :
            if num in hashmap : continue
            nleft, nright = num - 1, num + 1
            left = hashmap[nleft] if nleft in hashmap else 0
            right = hashmap[nright] if nright in hashmap else 0
            if left > 0 and right > 0 :
                hashmap[num] = hashmap[num - left] = hashmap[num + right] = left + right + 1
            elif left > 0 :
                hashmap[num] = hashmap[num - left] = left + 1
            elif right > 0 :
                hashmap[num] = hashmap[num + right] = right + 1
            else :
                hashmap[num] = 1
        print(hashmap)
        return max(hashmap.values()) if hashmap else 0

    # Solution 2 : hashset
    def sol2(self, nums) :
        hashset = set(nums)
        ans = 0
        for num in nums :
            if num - 1 not in hashset :
                l = 0
                while num in hashset : 
                    l += 1
                    num += 1
                ans = max(l, ans)
        return ans
        
# @lc code=end

