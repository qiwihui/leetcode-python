#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (32.91%)
# Likes:    1059
# Dislikes: 124
# Total Accepted:    114.9K
# Total Submissions: 344.8K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, num1, num2 = 0, 0, None, None
        
        for x in nums:
            if x == num1:
                count1 += 1
            elif x == num2:
                count2 += 1
            elif count1 == 0:
                num1 = x
                count1 = 1
            elif count2 == 0:
                num2 = x
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [n for n in (num1, num2) if nums.count(n) > len(nums) // 3]


# @lc code=end

