#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/description/
#
# algorithms
# Easy (27.81%)
# Likes:    375
# Dislikes: 233
# Total Accepted:    32.7K
# Total Submissions: 117.4K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings A and B of lowercase letters, return true if and only if we
# can swap two letters in A so that the result equals B.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: A = "ab", B = "ba"
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: A = "ab", B = "ab"
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: A = "aa", B = "aa"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: A = "", B = "aa"
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        # 相等且有重复字符
        if A == B and len(set(A)) < len(A):
            return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]

if __name__ == "__main__":
    print(Solution().buddyStrings("ab", "ab"))
    print(Solution().buddyStrings("aa", "aa"))

# @lc code=end

