class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return self.sol1(num)

    # Solution 1 :
    def sol1(self, num) :
        for i in range(1, len(num) // 2) :
            # if num[i] == 0 and i > 1 : continue
            for j in range(i + 1, len(num)) :
                # if num[j] == '0' and j - i > 1 : continue
                if self.dfs(num, 0 , i, j) : return True
        return False

    def dfs(self, num, i, j, k) :
        num1 = int(num[i : j])
        num2 = int(num[j : k])
        if str(num1) != num[i:j] or str(num2) != num[j:k] : return False
        addition = str(num1 + num2)
        if not num[k : ].startswith(addition) : return False
        if k + len(addition) == len(num) : return True
        return self.dfs(num, j, k, k + len(addition))

A = Solution()
print(A.isAdditiveNumber("12012122436"))