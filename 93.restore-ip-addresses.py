#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans, ip = [], ''
        self.dfs(0, s, ip, ans)
        return ans

    def dfs(self, d, s, ip, ans) :
        l = len(s)
        if d == 4 : 
            if l == 0 :
                ans.append(ip)
                return 

        for i in range(1, min(3, 1 if s[0] == '0' else l)) :
            ss = s[0 : i]
            if i == 3 or int(ss) > 255 : return 
            dfs(d + 1, s.substr(i), ip + (d == 0 ? "" : ".") + ss , ans);
    
        
# @lc code=end

