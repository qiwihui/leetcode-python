#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (73.42%)
# Likes:    1300
# Dislikes: 129
# Total Accepted:    258.5K
# Total Submissions: 352K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# You are given the root of a binary search tree (BST) and an integer val.
# 
# Find the node in the BST that the node's value equals val and return the
# subtree rooted with that node. If such a node does not exist, return null.
# 
# 
# Example 1:
# 
# 
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# 
# 
# Example 2:
# 
# 
# Input: root = [4,2,7,1,3], val = 5
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 10^7
# root is a binary search tree.
# 1 <= val <= 10^7
# 
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
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
# @lc code=end

