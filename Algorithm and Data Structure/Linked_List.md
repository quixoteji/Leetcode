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

Linked List vs Array
|   | Linked List  |Array |
|---|---|---|
|Insert/Delete|O(1)|O(n)|
|Random Access|O(n)|O(1)|

