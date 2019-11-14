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
```