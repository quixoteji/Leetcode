#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return self.sol2(nums)

    def sol1(self, nums) :
        n = len(nums) // 3
        hashmap = collections.defaultdict(int)
        hashset = set()
        ans = []
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > n and num not in hashset : 
                ans.append(num)
                hashset.add(num)        
        return ans

    def sol2(self, nums) :
        ans = []
        a, b, cnt1, cnt2 = float('inf'), float('inf'), 0, 0
        for num in nums :
            if num == a : cnt1 += 1
            elif num == b : cnt2 += 1
            elif cnt1 == 0 : 
                a = num
                cnt1 = 1
            elif cnt2 == 0 :
                b = num 
                cnt2 = 1
            else :
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums :
            if num == a : cnt1 += 1
            if num == b : cnt2 += 1

        if cnt1 > len(nums) // 3 : ans.append(a)
        if cnt2 > len(nums) // 3 : ans.append(b)
        return ans



        
# @lc code=end

