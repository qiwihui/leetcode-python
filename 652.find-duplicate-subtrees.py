#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (52.46%)
# Likes:    1833
# Dislikes: 237
# Total Accepted:    86K
# Total Submissions: 163.5K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given the root of a binary tree, return all duplicate subtrees.
# 
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
# 
# Two trees are duplicate if they have the same structure with the same node
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1,1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the tree will be in the range [1, 10^4]
# -200 <= Node.val <= 200
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
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # 思路：遍历所有节点，描述节点
        # 比较所有节点的描述
        self.res = []
        self.map = {}
        self.traverse(root)
        return self.res

    def traverse(self, node):
        if node is None:
            return '#'
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        node_map = f"{left},{right},{node.val}"
        freq = self.map.get(node_map, 0)
        if freq == 1:
            self.res.append(node)
        self.map[node_map] = freq + 1
        return node_map

# @lc code=end

