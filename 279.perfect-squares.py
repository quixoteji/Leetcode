#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        return self.sol3(n)

    # Solution 1 : dfs
    def sol1(self, n) :
        nums = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        ans = []
        self.dfs(ans, [], nums, n)
        return min(ans)

    def dfs(self, ans, curr, nums, n) :
        if sum(curr) == n :
            ans.append(len(curr))
            return
        if sum(curr) > n : return
        for num in nums :
            curr.append(num)
            self.dfs(ans, curr, nums, n)
            curr.pop()

    # Soluion 2 : dp
    def sol2(self, n) :
        nums = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1) :
            for num in nums :
                if i < num : break
                dp[i] = min(dp[i], dp[i - num] + 1)
        return dp[-1]

    # Solution 3 : greedy
    def sol3(self, n) :
        nums = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        level = 0
        queue = {n}
        while queue:
            level += 1
            #! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for num in nums:    
                    if remainder == num:
                        return level  # find the node!
                    elif remainder < num:
                        break
                    else:
                        next_queue.add(remainder - num)
            queue = next_queue
        return level 






        
        
# @lc code=end

