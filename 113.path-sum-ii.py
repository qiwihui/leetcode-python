#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (49.08%)
# Likes:    2575
# Dislikes: 85
# Total Accepted:    397.8K
# Total Submissions: 808.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return all
# root-to-leaf paths where each path's sum equals targetSum.
#
# A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
#
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1,2], targetSum = 0
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
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
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        if root.left is None and root.right is None and targetSum == root.val:
            return [[root.val]]

        temp = self.pathSum(root.left, targetSum-root.val) + self.pathSum(root.right, targetSum-root.val)
        return [[root.val]+i for i in temp]


# @lc code=end
if __name__ == "__main__":
    from ds_tree import build_from_level_order
    arr = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    root = build_from_level_order(arr, None, 0, len(arr)-1)
    print(root)
    print(Solution().pathSum(root, 22))