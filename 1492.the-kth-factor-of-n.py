#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#
# https://leetcode.com/problems/the-kth-factor-of-n/description/
#
# algorithms
# Medium (63.38%)
# Likes:    295
# Dislikes: 120
# Total Accepted:    43.9K
# Total Submissions: 69.4K
# Testcase Example:  '12\n3'
#
# Given two positive integers n and k.
# 
# A factor of an integer n is defined as an integer i where n % i == 0.
# 
# Consider a list of all factors of n sorted in ascending order, return the kth
# factor in this list or return -1 if n has less than k factors.
# 
# 
# Example 1:
# 
# 
# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
# 
# 
# Example 2:
# 
# 
# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.
# 
# 
# Example 3:
# 
# 
# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should
# return -1.
# 
# 
# Example 4:
# 
# 
# Input: n = 1, k = 1
# Output: 1
# Explanation: Factors list is [1], the 1st factor is 1.
# 
# 
# Example 5:
# 
# 
# Input: n = 1000, k = 3
# Output: 4
# Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125,
# 200, 250, 500, 1000].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= n <= 1000
# 
#
import math
import heapq

# @lc code=start
class Solution:

    # O(sqrt(N)), O(N)
    def kthFactor(self, n: int, k: int) -> int:
        # list all the factors, and use k-size BST to  and find the kth
        i = 1
        factors = []
        while i <= math.sqrt(n):
            if n % i == 0:
                heapq.heappush(factors, -i)
                if int(math.sqrt(n)) ** 2 != n:
                    heapq.heappush(factors, -n/i)
            i += 1
        while len(factors) > k:
            heapq.heappop(factors)
        
        if len(factors) < k:
            return -1
        return -int(heapq.heappop(factors))
    
    # O(N), O(1)
    def kthFactor_2(self, n: int, k: int) -> int:
        for i in range(1, n+1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        return -1
        
        
# @lc code=end
if __name__ == "__main__":
    print(Solution().kthFactor(12, 3) == 3)
    print(Solution().kthFactor(1000, 3) == 4)
    print(Solution().kthFactor(4, 4) == -1)
