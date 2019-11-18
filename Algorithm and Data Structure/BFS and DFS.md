# BFS and DFS

## BFS
```python
q.push(start)
step = 0

while not q.empty():
    ++step
    size = q.size()
    while size-- > 0 :
        node = q.pop()
        new_nodes = expand(node)
        if goal in new_nodes : return step + 1
        q.append(new_nodes)

return NOT_FOUND
```

## Bidirectional BFS

```python
s1.insert(start)
s2.insert(end)
step = 0

while not (s1.empty() || s2.empty()) :
    ++step
    swap(s1, s2)
    s = {}
    for node in s1 :
        new_nodes = expand(node)
        if any(new_nodes) in s2 : return step + 1
        s.append(new_nodes)
    s1 = s

return NOT_FOUND
```