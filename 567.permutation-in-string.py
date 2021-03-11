#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.59%)
# Likes:    2238
# Dislikes: 78
# Total Accepted:    177.5K
# Total Submissions: 398K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# 
# 
# Constraints:
# 
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}

        for i in s1:
            need.setdefault(i, 0)
            need[i] += 1

        left = right = 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1

            if c in need:
                window.setdefault(c, 0)
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # print(left, right)
            while right - left >= len(s1):
                d = s2[left]
                left += 1
                # 找到合法子串
                if valid == len(need):
                    return True

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
            
        return False
# @lc code=end

if __name__ == "__main__":
    print(Solution().checkInclusion("ab", "eidbaooo")==True)
    print(Solution().checkInclusion("ab", "eidboaoo"))
