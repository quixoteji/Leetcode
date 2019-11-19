# Permutation and Combination

## Permutation

```python
def Permutation(nums, d, used, curr, ans) :
    if d == len(nums) : 
        ans.append(curr)
        return
    for i in range(len(nums)) :
        if used[i] : continue
        used[i] = True
        curr.append(nums[i])
        Permutation(nums, d + 1, used, curr, ans)
        curr.pop()
        used[i] = False
```
### Permutation(all)
```python
class Solution:
    def dfs(self, ans, visited, nums) :
        if len(visited) == len(nums) :
            ans.append(visited[:])
            return 
        for num in nums :
            if num in visited : continue
            else :
                visited.append(num)
                self.dfs(ans, visited, nums)
                visited.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = []
        self.dfs(ans, visited, nums)
        return ans
```

### Permutation(Unique)
```python
class Solution:
    def dfs(self, ans, visited, curr, nums) :
        if len(curr) == len(nums) :
            ans.append(curr[:])
            return
        for i in range(len(nums)) :
            if i > 0 and nums[i] == nums[i-1] : continue
            # if i in visited : continue
            # visited.append(i)
            curr.append(nums[i])
            self.dfs(ans, visited, curr, nums)
            curr.pop()
            # visited.pop()

    def permuteUnique(self, nums):
        nums.sort()
        ans = []
        visited = []
        curr = []
        self.dfs(ans, visited, curr, nums)
        return ans
```

## Combination

```python
def Combination(nums, d, s, curr, ans) :
    if d == len(curr) :
        ans.append(curr)
        return

    for i in range(s, len(nums)) :
        curr.append(nums[i])
        Combination(nums, d + 1, i + 1, curr, ans)
        curr.pop()
```