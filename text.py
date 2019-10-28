class Solution:
    def generate(self, numRows):
        ans, n = [], 1
        while n <= numRows:
            curr = [1 for i in range(n)]
            if ans : curr[0] = curr[-1] = 1
            if n > 2 :
                for i in range(1, n - 1) : 
                    curr[i] = ans[n - 2][i - 1] + ans[n - 2][i]
            ans.append(curr[:])
            n += 1
        return ans
# -10,-3,0,5,9

A = Solution()
print(A.generate(5))