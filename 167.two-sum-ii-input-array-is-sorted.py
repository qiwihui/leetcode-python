#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (55.63%)
# Likes:    2428
# Dislikes: 695
# Total Accepted:    535K
# Total Submissions: 960.7K
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers numbers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
# 
# Return the indices of the two numbers (1-indexed) as an integer array answer
# of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# 
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Example 1:
# 
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# 
# 
# Example 2:
# 
# 
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# 
# 
# Example 3:
# 
# 
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in increasing order.
# -1000 <= target <= 1000
# Only one valid answer exists.
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s == target:
                return [lo+1, hi+1]
            elif s < target:
                lo += 1
            else:
                hi -= 1
        return []
        
# @lc code=end
if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(Solution().twoSum(numbers, target) == [1,2])
