#
# @lc app=leetcode id=710 lang=python3
#
# [710] Random Pick with Blacklist
#
# https://leetcode.com/problems/random-pick-with-blacklist/description/
#
# algorithms
# Hard (32.77%)
# Likes:    408
# Dislikes: 74
# Total Accepted:    17.4K
# Total Submissions: 52.8K
# Testcase Example:  '["Solution", "pick", "pick", "pick"]\n[[1, []], [], [], []]'
#
# Given a blacklist B containing unique integers from [0, N), write a function
# to return a uniform random integer from [0, N) which is NOT in B.
# 
# Optimize it such that it minimizes the call to system’s Math.random().
# 
# Note:
# 
# 
# 1 <= N <= 1000000000
# 0 <= B.length < min(100000, N)
# [0, N) does NOT include N. See interval notation.
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[1,[]],[],[],[]]
# Output: [null,0,0,0]
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[2,[]],[],[],[]]
# Output: [null,1,1,1]
# 
# 
# Example 3:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[3,[1]],[],[],[]]
# Output: [null,0,0,2]
# 
# 
# Example 4:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[4,[2]],[],[],[]]
# Output: [null,1,3,1]
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has two arguments, N and the blacklist B. pick has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
# 
#
from typing import List
import random
# @lc code=start
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.mappings = {}
        self.sz = N - len(blacklist)
        for b in blacklist:
            self.mappings[b] = -1
        last = N - 1
        for b in blacklist:
            # 如果 b 已经在区间 [sz, N)
            # 可以直接忽略
            if b >= self.sz:
                continue
            # 跳过所有黑名单中的数字
            while last in self.mappings:
                last -= 1
            self.mappings[b] = last
            last -= 1

    def pick(self) -> int:
        idx = random.randint(0, self.sz-1)
        if idx in self.mappings:
            return self.mappings[idx]
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
# @lc code=end

if __name__ == "__main__":
    s = Solution(2, [])
    print(s.pick())
