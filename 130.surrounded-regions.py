#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (29.40%)
# Likes:    2520
# Dislikes: 748
# Total Accepted:    284.5K
# Total Submissions: 967.6K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that
# any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is
# not on the border and it is not connected to an 'O' on the border will be
# flipped to 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
# 
# Example 2:
# 
# 
# Input: board = [["X"]]
# Output: [["X"]]
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# 
# 
#


# @lc code=start
from typing import List

class UnionFold(object):
    
    def __init__(self, num: int):
        # 树的大小
        self.size = [-1] * num
        # 联通分量个数
        self.count = num
        # 父节点
        self.parent = [-1] * num
        for i in range(num):
            self.parent[i] = i
            self.size[i] = 1

    def union(self, p: int, q: int):
        root_p = self._find(p)
        root_q = self._find(q)
        if root_p == root_q:
            return
        # 挂载
        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        # 联通量减小
        self.count -= 1

    def connected(self, p, q) -> bool:
        root_p = self._find(p)
        root_q = self._find(q)
        return root_p == root_q

    def _find(self, p) -> int:
        _p = p
        while self.parent[_p] != _p:
            self.parent[_p] = self.parent[self.parent[_p]]
            _p = self.parent[_p]
        return _p

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        uf = UnionFold(m*n+1)
        dummy = m*n
        # 搜索与边界联通的 “O”
        for i in range(0, m):
            for j in range(0, n):
                # the boundary
                if (i==0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == "O":
                    uf.union(i*n+j, dummy)
                elif board[i][j] == "O":
                    for l in [[1,0], [0, 1], [-1, 0], [0, -1]]:
                        x, y = l[0]+i, l[1]+j
                        if board[x][y] == "O":
                            uf.union(i*n+j, x*n+y)
        # 所有不和 dummy 连通的 O，都要被替换
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not uf.connected(dummy, i*n+j):
                    board[i][j] = "X"
# @lc code=end

if __name__ == "__main__":
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"],
        ["X","O","X","X"]
    ]
    Solution().solve(board)
    print(board == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"],["X","O","X","X"]])
