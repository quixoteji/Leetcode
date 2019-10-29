class Solution:
    def dfs(self, ans, curr, d, i, T) :
        if d == len(T) - 1: 
            curr.append(T[d][i])
            ans.append(curr[:])
            return
        curr.append(T[d][i])
        self.dfs(ans, curr, d + 1, i, T)
        curr.pop()
        if d > 0 :
            self.dfs(ans, curr, d + 1, i + 1, T)
            curr.pop()

    def minimumTotal(self, triangle) :
        if len(triangle) == 0 : return 0 
        ans = []
        curr = [
        val = 0
        d, i = 0, 0
        self.dfs(ans, curr, d, i, triangle)
        return ans  
# -10,-3,0,5,9

A = Solution()
print(len([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(A.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))