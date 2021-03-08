#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (51.80%)
# Likes:    4816
# Dislikes: 123
# Total Accepted:    466.1K
# Total Submissions: 897.4K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
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


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # value to key mapping
        self.in_map = {val:i for i, val in enumerate(inorder)}
        self.preorder = preorder
        self.inorder = inorder
        return self.travese(0, 0, len(inorder)-1)

    def travese(self, pre_root_idx, in_left_idx, in_right_idx):
        if in_left_idx > in_right_idx:
            return None
        
        root = TreeNode(self.preorder[pre_root_idx])
        # 根据前序值，在中序获取对应值的idx
        idx = self.in_map[self.preorder[pre_root_idx]]
        
        root.left = self.travese(pre_root_idx+1, in_left_idx, idx-1)
        root.right = self.travese(pre_root_idx + (idx-in_left_idx) + 1, idx+1, in_right_idx)

        return root


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.in_map = {val:i for i, val in enumerate(inorder)}
        return self.build(
            preorder, 0, len(preorder)-1,
            inorder, 0, len(inorder)-1,
        )

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end:
            return None

        root = TreeNode(preorder[pre_start])
        in_root_idx = self.in_map[preorder[pre_start]]

        left_size = in_root_idx - in_start
        root.left = self.build(
            preorder, pre_start+1, pre_start+left_size,
            inorder, in_start, in_root_idx-1,
        )
        root.right = self.build(
            preorder, pre_start+left_size+1, pre_end,
            inorder, in_root_idx+1, in_end,
        )

        return root

# @lc code=end

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    tree = Solution2().buildTree(preorder, inorder)
    print(tree)

