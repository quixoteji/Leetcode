# Linked List

## Cache Strategy
- FIFO: First In, First Out
- LFU: Least Frequently Used
- LRU: Least Recently Used

## Types
- Single Linked List
- Doubly Linked List
- Circular Linked List
```python
# Single Linked List Node
class SingleLinkedList :
    def __init__(self, val):
        self.val = val
        self.next = None

class DoublyLinkedList :
    def __init__(self, val) :
        self.val = val
        self.next = None
        self.prev = None
```

## Linked List vs Array

|   | Linked List  |Array |
|---|---|---|
|Insert/Delete|O(1)|O(n)|
|Random Access|O(n)|O(1)|

## Snippets

### Get Middle Node of Linked List
```python
def getMiddle(head) : 
    prev = fast = slow = head
    while fast and fast.next : 
        prev = slow
        slow, fast = slow.next, fast.next.next
    prev.next = None
    return slow
```

### Remove Elements
```python
def removeElement(head, val) :
    dummy = ListNode(0)
    dummy.next = head
    prev, curr = dummy, head
    while curr :
        if curr.val == val : prev.next = curr.next
        else : prev = curr
        curr = curr.next

    return dummy.next
```

### Delete Node in a Linked List
```python
def deleteNode(node) :
    temp = node.next
    node.val = temp.val
    node.next = node.next.next
```

### Swap Nodes in Pairs
```python
# Iteration
def swap(head) :
    if not head or not head.next : return head
    dummy = prev = ListNode(0)
    dummy.next = head
    while prev.next and prev.next.next :
        temp = prev.next.next
        prev.next.next = temp.next
        temp.next = prev.next
        prev.next = temp
        prev = temp.next
    return dummy.next
# Recursion
def swap(head) :
    if not head or not head.next : return head
    temp = head.next.next
    first, second = head, head.next
    second.next = first
    first.next = swap(temp)
    return second
```

### Reverse Linked List
```python
def reverseLinkedList(head) :
    if not head or not head.next : return head
    curr, prev = head, None
    while curr :
        nextTemp = curr.next
        curr.next = prev
        curr, prev = nextTemp, curr
    return prev

def reverseLinkedList(head) :
    if not head or not head.next : return head
    dummy = ListNode(0)
    dummy.next = head
    while head and head.next :
        temp = head.next
        head.next = temp.next
        temp.next = dummy.next
        dummy.next = temp
    return dummy.next

def reverseLinkedList(head) :
    prev, curr = None, head
    while curr :
        prev, curr.next, curr = curr, prev, curr.next
    return prev

def reverseLinkedList(head) :
    if not head or not head.next : return head
    p = self.reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return p
        
```

### Insertion Sort List
```python
def insertionSortList(head) :
    if not head or not head.next : return head
    prev = ListNode(0)
    while head :
        temp = head.next
        curr = prev
        while curr.next and curr.next.val <= head.val :
            curr = curr.next
        head.next = curr.next
        curr.next = head
        head = temp
    return prev.next
```

### Merge Sort List
```python
    def mergeSort(self, head) :
        if not head or not head.next : return head
        slow = self.getMiddle(head)
        left = self.mergeSort(head)
        right = self.mergeSort(slow)
        return self.merge(left, right)
    
    def getMiddle(self, head) :
        prev = slow = fast = head
        while fast and fast.next :
            prev = slow
            slow, fast = slow.next, fast.next.next
        prev.next = None
        return slow
    
    def merge(self, left, right) :
        prev = head = ListNode(0)
        while left and right :
            if left.val < right.val :
                prev.next = left
                left = left.next
            else :
                prev.next = right
                right = right.next
            prev = prev.next
        if left : prev.next = left
        if right : prev.next = right
        return head.next
    
```