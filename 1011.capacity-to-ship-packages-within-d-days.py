#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
#
# algorithms
# Medium (59.68%)
# Likes:    1857
# Dislikes: 56
# Total Accepted:    66.8K
# Total Submissions: 111.9K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n5'
#
# A conveyor belt has packages that must be shipped from one port to another
# within D days.
# 
# The i^th package on the conveyor belt has a weight of weights[i]. Each day,
# we load the ship with packages on the conveyor belt (in the order given by
# weights). We may not load more weight than the maximum weight capacity of the
# ship.
# 
# Return the least weight capacity of the ship that will result in all the
# packages on the conveyor belt being shipped within D days.
# 
# 
# Example 1:
# 
# 
# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in
# 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# 
# Note that the cargo must be shipped in the order given, so using a ship of
# capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6,
# 7), (8), (9), (10) is not allowed.
# 
# 
# Example 2:
# 
# 
# Input: weights = [3,2,2,4,1,4], D = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in
# 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# 
# 
# Example 3:
# 
# 
# Input: weights = [1,2,3,1,1], D = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= D <= weights.length <= 5 * 10^4
# 1 <= weights[i] <= 500
# 
# 
#

# @lc code=start
from typing import List

def can_hold(weights, D, cap):
    day = 0
    su = 0
    for w in weights:
        # print(w, su, day)
        su += w
        if su > cap:
            day += 1
            su = w
            if day > D:
                return False
    if su > 0:
        day += 1
    if day > D:
        return False
    return True


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights) + 1
        while left < right:
            mid = (left+right) // 2
            if can_hold(weights, D, mid):
                right = mid
            else:
                left = mid + 1
            # print(left, right)
        return left
# @lc code=end

if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    print(Solution().shipWithinDays(weights, D) == 15)

    # print(can_hold(weights, 5, 14))