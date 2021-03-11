#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (56.26%)
# Likes:    1922
# Dislikes: 149
# Total Accepted:    183.5K
# Total Submissions: 326K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given the root of a Binary Search Tree and a target number k, return true if
# there exist two elements in the BST such that their sum is equal to the given
# target.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: root = [2,1,3], k = 4
# Output: true
# 
# 
# Example 4:
# 
# 
# Input: root = [2,1,3], k = 1
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: root = [2,1,3], k = 3
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# root is guaranteed to be a valid binary search tree.
# -10^5 <= k <= 10^5
# 
# 
#
from ds_tree import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # 遍历，记录已经访问内容
        # Time: O(N), Space: O(N)
        return self.traverse(root, set(), k)
        # 前序列遍历，转换成对排序的数组问题，利用双指针处理
        # Time: O(N), Space: O(N)
    
    def traverse(self, root, visited, k):
        if root is None:
            return False
        
        if (k - root.val) in visited:
            return True
        else:
            visited.add(root.val)
        return self.traverse(root.left, visited, k) or self.traverse(root.right, visited, k)
        
# @lc code=end
if __name__ == "__main__":
    print(Solution().findTarget(TreeNode(1), 2))
