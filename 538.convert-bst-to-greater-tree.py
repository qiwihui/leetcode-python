#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Medium (59.37%)
# Likes:    2525
# Dislikes: 144
# Total Accepted:    161K
# Total Submissions: 270.6K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
# such that every key of the original BST is changed to the original key plus
# sum of all keys greater than the original key in BST.
# 
# As a reminder, a binary search tree is a tree that satisfies these
# constraints:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# Note: This question is the same as 1038:
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# 
# 
# Example 1:
# 
# 
# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# 
# Example 2:
# 
# 
# Input: root = [0,null,1]
# Output: [1,null,1]
# 
# 
# Example 3:
# 
# 
# Input: root = [1,0,2]
# Output: [3,3,2]
# 
# 
# Example 4:
# 
# 
# Input: root = [3,2,4,1]
# Output: [7,9,4,10]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -10^4 <= Node.val <= 10^4
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        return self.traverse(root)

    def traverse(self, root):
        if root is None:
            return None
        self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        self.traverse(root.left)
        return root
# @lc code=end

