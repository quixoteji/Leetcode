class Solution:
    def countAndSay(self, n):
        if n == 1 : return "1"
        ans = "1"
        for x in range(2, n + 1):
            temp = ''
            t, char = 0, ''
            for i in range(len(ans)) :
                if i == 0 : 
                    t += 1
                    char = ans[0]
                else :
                    if ans[i] == ans[i - 1] : 
                        t += 1
                    else :
                        temp += str(t) + char
                        t = 1
                        char = ans[i]
            ans = temp + str(t) + char
        return ans

A = Solution()
print(A.countAndSay(6))