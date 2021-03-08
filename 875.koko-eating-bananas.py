#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (53.49%)
# Likes:    1310
# Dislikes: 82
# Total Accepted:    62.8K
# Total Submissions: 117.5K
# Testcase Example:  '[3,6,7,11]\r\n8\r'
#
# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has
# piles[i] bananas.  The guards have gone and will come back in H hours.
# 
# Koko can decide her bananas-per-hour eating speed of K.  Each hour, she
# chooses some pile of bananas, and eats K bananas from that pile.  If the pile
# has less than K bananas, she eats all of them instead, and won't eat any more
# bananas during this hour.
# 
# Koko likes to eat slowly, but still wants to finish eating all the bananas
# before the guards come back.
# 
# Return the minimum integer K such that she can eat all the bananas within H
# hours.
# 
# 
# Example 1:
# Input: piles = [3,6,7,11], H = 8
# Output: 4
# Example 2:
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# Example 3:
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
# 
# 
# Constraints:
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
#

# @lc code=start
from typing import List

def can_finish(piles, speed, H):
    spent = 0
    for p in piles:
        spent += p // speed if p%speed == 0 else p // speed + 1
    return spent <= H


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles) + 1
        while left < right:
            mid = (left + right) // 2
            if can_finish(piles, mid, H):
                right = mid
            else:
                left = mid + 1
        return left

        
# @lc code=end

if __name__ == "__main__":
    print(Solution().minEatingSpeed([3,6,7,11], 8) == 4)
    print(Solution().minEatingSpeed([30,11,23,4,20], 5) == 30)
    print(Solution().minEatingSpeed([30,11,23,4,20], 6) == 23)
