# 01 Tree

## 1 Traverse
- preorder
```
def preorder(root) : 
    return [root.val] + self.preorder(root.left) + self.preorder(root.right) if root else []

def preorder(root) : 
    if not root : return []
    ans, stack = [], [root]
    while stack :
        root = stack.pop()
        ans.append(root.val)
        if root.right : stack.append(root.right)
        if root.left : stack.append(root.left)
    return ans
```
- inorder
```
def inorder(root) :
    return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

def inorder(root) :
    if not root : return []
    ans, stack = [], []
    while stack or root :
        while root :
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans.append(root.val)
        root = root.right
    return ans
```
- postorder
```
def postorder(root) :
    return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []

def postorder(root) :
    if not root : return []
    ans, stack = [], [root]
    while stack :
        root = stack.pop()
        ans.append(root.val)
        if root.left : ans.append(root.left)
        if root.right : ans.append(root.right)
    return ans[::-1]
```
- Level Traverse
```
def traverse(root) :
    if not root : return []
    ans, queue = [], [root]
    while queue :
        l = len(queue)
        level = []
        for _ in range(l) :
            node = queue.pop(0)
            level.append(node.val)
            if node.left : queue.append(node.left)
            if node.right : queue.append(node.right)
        ans.append(level)
    return ans
```