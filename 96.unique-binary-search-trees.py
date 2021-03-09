#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (54.42%)
# Likes:    4379
# Dislikes: 162
# Total Accepted:    351.5K
# Total Submissions: 645.2K
# Testcase Example:  '3'
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 19
# 
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        self.mem = {}
        return self.count(1, n)
    
    def count(self, lo, hi):
        if lo > hi:
            return 1
        if f"{lo}-{hi}" in self.mem:
            return self.mem[f"{lo}-{hi}"]
        res = 0
        for i in range(lo, hi+1):
            left = self.count(lo, i-1)
            right = self.count(i+1, hi)
            res += left * right
        self.mem[f"{lo}-{hi}"] = res
        return res
        
# @lc code=end

