#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        left=self.serialize(root.left)
        right=self.serialize(root.right)
        serialized= str(root.val)+'R'+'['+left+']'+right
        return serialized
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        left_index=data.index('R')
        root=TreeNode(int(data[:left_index]))
        lr=data[left_index+1:]
        l,r=0,0
        right_index=-1
        for i in range(len(lr)):
            if lr[i]=='[':
                l+=1
            elif lr[i]==']':
                r+=1
            if l==r:
                right_index=i
                break
        left_line=lr[1:right_index]
        root.left=self.deserialize(left_line)
        right_line=lr[right_index+1:]
        root.right=self.deserialize(right_line)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

