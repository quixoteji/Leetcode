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