#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (59.37%)
# Likes:    2095
# Dislikes: 35
# Total Accepted:    371.1K
# Total Submissions: 618.7K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Invert a binary tree.
# 
# Example:
# 
# Input:
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
# 
# Output:
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
# 
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# 
# Google: 90% of our engineers use the software you wrote (Homebrew), but you
# can’t invert a binary tree on a whiteboard so f*** off.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self._travase(root)
        # return self._bfs(root)

    def _bfs(self, root):
        if not root:
            return None
        
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
    
    def _travase(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self._travase(root.left)
        self._travase(root.right)
        return root
        
        
# @lc code=end

