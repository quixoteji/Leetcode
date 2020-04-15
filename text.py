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
    def sortedListToBST(self, head) :
        if not head or not head.next : return head
        prev = slow = fast = ListNode(0)
        prev.next = head
        while fast and fast.next :
            slow, fast = slow.next, fast.next.next
            
        root = TreeNode(slow.val)
        temp = slow.next
        slow.next = None
        # print(type(root))
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp)
        
        return root

# [-10,-3,0,5,9]
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

a = Solution()
a.sortedListToBST(head)