#
# @lc app=leetcode id=247 lang=python3
#
# [247] Strobogrammatic Number II
#

# @lc code=start
class Solution:
    # Solution1
    def isStro(self, num) :
        if not num : return True
        hashmap = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9' : '6'}
        
        l, r = 0, len(num) - 1
        while l <= r :
            if num[l] not in hashmap or hashmap[num[l]] != num[r] : return False
            l, r = l + 1, r - 1
        return True

    def dfs(self, ans, s, n, nums) :
        if len(s) == n :
            if self.isStro(s):
                if str(int(s)) == s :
                    ans.append(s)
            return
        for num in nums :
            self.dfs(ans, s + num, n, nums)

        
    def backtracking(self, n) :
        nums = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9' : '6'}
        ans = []
        if n == 0 : return ans
        self.dfs(ans, '', n, nums)
        return ans

    # Solution 2
    def dfs(self, ans, s, n, strobo) :
        if len(s) == n :
            if str(int(s)) == s :
                ans.append(s)
            return 
        for num in strobo :
            self.dfs(ans, num + s + strobo[num], n, strobo)
        return

    def backtrack2(self, n) :
        strobo = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9' : '6'}
        ans = []
        if n == 0 : return ans
        if n % 2 == 0 : 
            self.dfs(ans, '', n, strobo)
        if n % 2 == 1 :
            for num in ['0', '1', '8'] :
                self.dfs(ans, num, n, strobo)
        return ans

    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.backtrack2(n)

        
# @lc code=end

