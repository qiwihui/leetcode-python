#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (49.85%)
# Likes:    1846
# Dislikes: 48
# Total Accepted:    446.4K
# Total Submissions: 884.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.

from typing import List

import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        # return self.levelOrder_BFS(root)
        return self.levelOrder_DFS(root)

    def levelOrder_DFS(self, root: TreeNode):
        """使用DFS解决，T(n)=O(n)
        """
        self.result = []
        # DFS helper
        def helper(node, level):
            if not node:
                return
            # 确保存在对应层数组
            if len(self.result) < level+1:
                self.result.append([])
            
            self.result[level].append(node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)

        helper(root, 0)
        return self.result

    def levelOrder_BFS(self, root: TreeNode):
        """使用BFS解决，T(n)=O(n)
        """
        if not root:
            return []
        # BFS
        queue = collections.deque()
        queue.append(root)

        traversal = []

        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            traversal.append(level)

        return traversal


# @lc code=end

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # [[3],[9,20],[15,7]]
    print(Solution().levelOrder(root))
