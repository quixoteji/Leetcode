import collections

class Solution:
    def solve(self, nums) :
        ans = []
        a, b, cnt1, cnt2 = 0, 0, 0, 0
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

        if cnt1 > n // 3 : ans.append(a)
        if cnt2 > n // 3 : ans.append(b)
        return ans
            
A = Solution()
print(A.solve([3,2,3,2,2,3,4,4,4,4,4]))
