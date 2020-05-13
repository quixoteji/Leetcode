# Code Snippets

### Binary Search Template
```python
# Returns the smallest m in [l, r)
# s.t. cond(m) == True
# if not returns r
def binarysearch(l, r) :
    m = l + (r - l) // 2
    if cond(m) : r = m
    else  : l = m + 1
    return l
```

### Permutation
```python
def P(n, m, cur, used) :
    if len(cur) == m :
        print(cur)
        return
    for i in range(n) :
        if used[i] : continue
        used[i] = True
        cur.append(i + 1)
        P(n, m, cur), used
```