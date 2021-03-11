#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (49.78%)
# Likes:    4037
# Dislikes: 187
# Total Accepted:    419.7K
# Total Submissions: 841.2K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: root = [1,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    前序
    后序
    层级遍历
    """
    null = "NULL"
    sep = ","

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        self.traverse_level(root)
        return self.sep.join(self.res)

    def traverse(self, root):
        if root is None:
            self.res.append(self.null)
            return
        self.res.append(str(root.val))
        self.traverse(root.left)
        self.traverse(root.right)
    
    def traverse_level(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node is None:
                self.res.append(self.null)
                continue
            self.res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.res = data.split(self.sep)
        return self._deserialize_level(self.res)

    def _deserialize(self, res: list):
        if not res:
            return None
        node = res.pop(0)
        if node == self.null:
            return None
        root = TreeNode(int(node))
        root.left = self._deserialize(res)
        root.right = self._deserialize(res)
        return root
    
    def _deserialize_level(self, res: list):
        if not res or not res[0]:
            return None
        queue = []
        root = TreeNode(int(res[0]))
        queue.append(root)
        
        i = 0
        while i < len(res):
            if not queue:
                break
            node = queue.pop(0)
            i += 1
            left = res[i]
            if left == self.null:
                node.left = None
            else:
                node.left = TreeNode(int(left))
                queue.append(node.left)
            
            i += 1
            right = res[i]
            if right == self.null:
                node.right = None
            else:
                node.right = TreeNode(int(right))
                queue.append(node.right)
        return root




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
