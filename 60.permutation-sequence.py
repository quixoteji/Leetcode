#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
from math import factorial as f
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.sol3(n, k)

    # Solution 1 : dfs then pick
    def sol1(self, n, k) :
        ans = []
        self.dfs(ans, '', n) 
        # print(ans)
        return ans[k - 1]
    
    def dfs(self, ans, curr, n) :
        if len(curr) == n : 
            ans.append(curr)
            return 
        for i in range(1, n + 1) :
            if str(i) in curr : continue
            self.dfs(ans, curr + str(i), n)

    # Solution 2 : dfs index
    ans = ''
    idx = 1

    def sol2(self, n, k) :
        self.ddfs('', n, k)
        return self.ans
    def ddfs(self, curr, n, k) :
        if self.idx > k : return
        if len(curr) == n : 
            if self.idx == k : self.ans = curr    
            self.idx += 1
            return 
        for i in range(1, n + 1) :
            if str(i) in curr : continue
            self.ddfs(curr + str(i), n, k)

    def sol3(self, n, k) :
        nums = [i + 1 for i in range(n)]
        ans = ''
        while nums :
            j = f(len(nums)-1)
            place = (k-1)//j
            ans += str(nums[place])
            nums.pop(place)
            k = k - (place * j)
        return ans
        
# @lc code=end

