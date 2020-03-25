#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#

# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        return self.sol1(n, k) 

    def sol1(self, n, k) :
        pre=1 
        pos=1
        while pos < k:
            cnt = self.count(pre,n)
            if pos+cnt>k:
                pre *= 10
                pos += 1
            else:
                pre += 1
                pos += cnt
        return pre
        
    #以pre为前缀的数字个数
    def count(self,pre,n):
        cnt = 0
        a = pre
        b = pre+1
        while a <= n:
            cnt += min(n+1,b) - a #左闭右开，所以不会额外+1
            #update next a,b
            a *= 10
            b *= 10
        return cnt
        
# @lc code=end

