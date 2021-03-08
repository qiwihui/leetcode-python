#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (49.64%)
# Likes:    2478
# Dislikes: 48
# Total Accepted:    284.5K
# Total Submissions: 571.7K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given two integer arrays inorder and postorder where inorder is the inorder
# traversal of a binary tree and postorder is the postorder traversal of the
# same tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# 
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# 
# Input: inorder = [-1], postorder = [-1]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.
# 
# 
#
from typing import List
from ds_tree import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        pass


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.in_map = {val:i for i, val in enumerate(inorder)}
        return self.build(
            inorder, 0, len(inorder)-1,
            postorder, 0, len(postorder)-1,
        )

    def build(self, inorder, in_start, in_end, postorder, post_start, post_end):
        if in_start > in_end:
            return None

        root = TreeNode(postorder[post_end])
        in_root_idx = self.in_map[postorder[post_end]]

        left_size = in_root_idx - in_start
        root.left = self.build(
            inorder, in_start, in_root_idx-1,
            postorder, post_start, post_start+left_size-1,
        )
        root.right = self.build(
            inorder, in_root_idx+1, in_end,
            postorder, post_start+left_size, post_end-1,
        )

        return root
# @lc code=end

if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    tree = Solution().buildTree(inorder, postorder)
    print(tree)
