#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#
# https://leetcode.com/problems/find-the-town-judge/description/
#
# algorithms
# Easy (49.41%)
# Likes:    259
# Dislikes: 37
# Total Accepted:    31.1K
# Total Submissions: 62.8K
# Testcase Example:  '2\n[[1,2]]'
#
# In a town, there are N people labelled from 1 to N.  There is a rumor that
# one of these people is secretly the town judge.
#
# If the town judge exists, then:
#
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
#
#
# You are given trust, an array of pairs trust[i] = [a, b] representing that
# the person labelled a trusts the person labelled b.
#
# If the town judge exists and can be identified, return the label of the town
# judge.  Otherwise, return -1.
#
#
#
# Example 1:
#
#
# Input: N = 2, trust = [[1,2]]
# Output: 2
#
#
#
# Example 2:
#
#
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
#
#
#
# Example 3:
#
#
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
#
#
#
# Example 4:
#
#
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
#
#
#
# Example 5:
#
#
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
#
#
#
#
#
#
#
# Note:
#
#
# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N
#
#
#

from typing import List


# @lc code=start
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # 计算所有点的 入度-出度，为 N-1 的就是
        res = [0] * (N + 1)
        for i, j in trust:
            res[i] -= 1
            res[j] += 1
        for v in range(1, N + 1):
            if res[v] == N - 1:
                return v
        return -1


# @lc code=end

if __name__ == "__main__":
    cases = [
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
        (3, [[1, 2], [2, 3]], -1),
        (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3),
    ]
    for N, trust, res in cases:
        assert (res == Solution().findJudge(N, trust))
