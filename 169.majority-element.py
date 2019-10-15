#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (53.86%)
# Likes:    2026
# Dislikes: 178
# Total Accepted:    446.5K
# Total Submissions: 820.3K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 分治
        n = len(nums)
        if n == 1:
            return nums[0]
        left = self.majorityElement(nums[:n//2])
        right = self.majorityElement(nums[n//2:])
        if left == right:
            return left
        else:
            left_count = sum(1 for i in nums if left == i)
            right_count = sum(1 for i in nums if right == i)
            return left if left_count > right_count else right

        
# @lc code=end

