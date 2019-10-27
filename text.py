# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def splitList(self, head) :
        dummy, l = head, 0
        while dummy : dummy, l = dummy.next, l + 1
        idx = (l - 1) // 2
        prev = ListNode(0)
        prev.next = head
        curr = head
        n = 0
        while n < idx :
            prev, curr, n = prev.next, curr.next, n + 1
        prev.next = None
        return curr, head, curr.next

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head : return None
        r, left, right = self.splitList(head)
        root = TreeNode(r.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root
# -10,-3,0,5,9
head = ListNode(-10)
t1 = ListNode(-3)
t2 = ListNode(0)
t3 = ListNode(5)
t4 = ListNode(9)

head.next = t1
t1.next = t2
t2.next = t3
t3.next = t4

A = Solution()
print(A.sortedListToBST(head))