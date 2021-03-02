#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#
# https://leetcode.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (56.48%)
# Likes:    179
# Dislikes: 232
# Total Accepted:    14K
# Total Submissions: 24.5K
# Testcase Example:  '[[2]]'
#
# On a N * N grid, we place some 1 * 1 * 1 cubes.
# 
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid
# cell (i, j).
# 
# Return the total surface area of the resulting shapes.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[2]]
# Output: 10
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[3,4]]
# Output: 34
# 
# 
# 
# Example 3:
# 
# 
# Input: [[1,0],[0,2]]
# Output: 16
# 
# 
# 
# Example 4:
# 
# 
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
# 
# 
# 
# Example 5:
# 
# 
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    # 最上和最下
                    ans += 2
                    # 判断上下左右的情况
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        # 计算多出来的面积
                        ans += max(grid[r][c] - nval, 0)
        return ans

# @lc code=end

