#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = self.rserialize(root, '')
        print(ans)
        return ans

    def rserialize(self, root, s) :
        if not root : s += '*'
        else : s += str(root.val) + ',' + self.rserialize(root.left, s) + ',' + self.rserialize(root.right, s)
        return s


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self.rdeserialize(data.split(','))

    def rdeserialize(self, data) :
        if data[0] == '*' : 
            data.pop(0)
            return None
        root = TreeNode(int(data[0]))
        data.pop(0)
        root.left = self.rdeserialize(data)
        root.right = self.rdeserialize(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

