#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (49.26%)
# Likes:    2755
# Dislikes: 250
# Total Accepted:    283.1K
# Total Submissions: 573.5K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
# 
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at the last
# level h.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,6]
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
# 
# 
# 
# Follow up: Traversing the tree to count the number of nodes in the tree is an
# easy solution but with O(n) complexity. Could you find a faster algorithm?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        l = root
        r = root
        h = 0
        while r is not None:
            l = l.left
            r = r.right
            h += 1
        if l is None:
            return (1 << h) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
# @lc code=end

