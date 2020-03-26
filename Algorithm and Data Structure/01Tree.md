# Tree

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
- Morris Traversal

## 2 Binary Search Tree
- Search in a BST
```
def search(root, val) : 
    if not root or root.val == val : return root
    return self.search(root.left, val) if root.val > val else self.search(root.right, val)

def search(root, val) :
    while root and root.val != val :
        root = root.left if root.val > val else root.right
    return root
```
- Insert in a BST
```
def insert(root, val) :
    if not root : return TreeNode(val)
    elif val > root.val : root.right = self.insert(root.right, val)
    elif val < root.val : root.left = self.insert(root.left, val)
    return root

def insert(root, val) : 
    node = root
    while node :
        if val > node.val : 
            if not node.right : 
                node.right = TreeNode(val)
                return root
            else :
                node = node.right
        else :
            if not node.left :
                node.left = TreeNode(val)
                return root
            else :
                node = node.left
    return TreeNode(val)
```

- Delete in a BST
```
def delete(root, key) : 
    def successor(node) :
        node = node.right
        while node.left :
            node = node.left
        return node.val
    def predecessor(node) :
        node = node.left
        while node.right :
            node = node.right
        return node.val
    if not root : return None
    elif key > root.val : 
        self.delete(root.right, key)
    elif key < root.val :
        self.delete(root.left, key)
    else : 
        if not root.right and not root.left : 
            return None
        elif root.right :
            root.val = successor(root)
            root.right = self.delete(root.right, root.val)
        elif root.left :
            root.val = predecessor(root)
            root.left = self.delete(root.left, root.val)
    return root
```

- **Split a BST**
```
def split(root, key) :
    if not root : return [None, None]
    elif root.val <= key :
        bns = self.split(root.right, key)
        root.right = bns[0]
        return [root, bns[1]]
    else :
        bns = self.split(root.left, key)
        root.left = bns[1]
        return [bns[0], root]
```
