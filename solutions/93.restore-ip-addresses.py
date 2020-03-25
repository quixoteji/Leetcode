#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.sol2(s)

    # Solution 1:
    def sol1(self, s) :
        ans = []
        for i in range(1, 4) :
            if i >= len(s) : continue
            if int(s[:i]) > 255 or str(int(s[:i])) != s[:i] : continue
            for j in range(i + 1, i + 4) :
                if j >= len(s) : continue
                if int(s[i:j]) > 255 or str(int(s[i:j])) != s[i:j] : continue
                for k in range(j + 1, j + 4):
                    if k >= len(s) : continue
                    if int(s[j:k]) > 255 or str(int(s[j:k])) != s[j:k] : continue
                    if int(s[k:]) > 255 or str(int(s[k:])) != s[k:]: continue
                    ans.append(s[:i]+'.'+s[i:j]+'.'+s[j:k]+'.'+s[k:])
        return ans
         
    # Solution 2 :
    def sol2(self, s) : 
        ans = []
        self.dfs(ans, [], s)
        return ans

    def dfs(self, ans, curr, s) :
        if not s and len(curr) == 4 :
            ans.append('.'.join(curr))
            return 
        if not s or len(curr) >= 4: return
        for i in range(1, 4) :
            if i > len(s) : break
            t = s[:i]
            if t != str(int(t)) or int(t) > 255 : continue
            curr.append(t)
            self.dfs(ans, curr, s[i:])
            curr.pop()


    
        
# @lc code=end

