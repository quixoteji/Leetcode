# Disjoint-set / Union-find Forest

## Main Functions
Find(x) : find the root / cluster-id of x
Union(x, y) : merge two clusters

## Motivation
Check whether two elements are in the same set or not in O(1)
- Find : O(a(n)) = O(1)
- Union : O(a(n)) = O(1)
- Space : O(n)

*Without optimization : Find O(n)*

## Two key optimization
Two Key optimizations : 
1. Path compression : make tree flat
2. Union by rank : merge low rank tree to high rank one

```python
class UnionFindSet():
    def __init__(self, n) :
        parents = [i for i in range(1, n + 1)]
        ranks = [0 for i in range(n)]

    def find(self, x) :
        if x != self.parents[x] :
            self.parents[x] = self.find(parents[x])
        return self.parents[x]

    def union(self, x, y) :
        px, py = self.find(x), self.find(y)
        if self.ranks[px] > self.ranks[py] :
            self.parents[px] = px
        elif self.ranks[px] < self.ranks[py] :
            self.parents[px] = py
        else :
            self.parents[py] = px
            self.ranks[px] += 1
        return True 
```
