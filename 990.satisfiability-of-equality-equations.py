#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (45.91%)
# Likes:    746
# Dislikes: 6
# Total Accepted:    26.3K
# Total Submissions: 56.2K
# Testcase Example:  '["a==b","b!=a"]'
#
# Given an array equations of strings that represent relationships between
# variables, each string equations[i] has length 4 and takes one of two
# different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not
# necessarily different) that represent one-letter variable names.
# 
# Return true if and only if it is possible to assign integers to variable
# names so as to satisfy all the given equations.
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
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.  There is no way to assign the variables to
# satisfy both equations.
# 
# 
# 
# Example 2:
# 
# 
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# 
# 
# 
# Example 3:
# 
# 
# Input: ["a==b","b==c","a==c"]
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: ["a==b","b!=c","c==a"]
# Output: false
# 
# 
# 
# Example 5:
# 
# 
# Input: ["c==c","b==d","x!=z"]
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='
# 
# 
# 
# 
# 
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

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFold(26)
        N = ord('a')
        for eq in equations:
            if eq[1] == "=":
                uf.union(ord(eq[0])-N, ord(eq[3])-N)
        
        for eq in equations:
            if eq[1] == "!":
                connected = uf.connected(ord(eq[0])-N, ord(eq[3])-N)
                if connected:
                    return False
        return True
        
# @lc code=end

if __name__ == "__main__":
    equations = ["f==a","a==b","f!=e","a==c","b==e","c==f"]
    print(Solution().equationsPossible(equations))
