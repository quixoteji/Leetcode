def dfs(ans, curr, nums, idx, k) :
    if len(curr) == k : 
        ans.append(curr[:])
        return
    for num in nums[idx : ]:
        curr.append(num)
        dfs(ans, curr, nums, idx + 1, k)
        curr.pop()
        

def combine(n, k) :
    nums = [i for i in range(1, n + 1)]
    ans, curr = [], []
    dfs(ans, curr, nums, 0, k)
    return ans


print(combine(4, 2))

