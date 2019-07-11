#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring, length, max_len = "", 0, 0
        # At the beginning, our substring is empty. Then
        # we can iteratively add new characters to the substring.
        for c in s:
            # If duplicated characters appear, we have to cut off
            # all the letters before the duplicated one, including
            # the one that is duplicated, from our substring, in
            # order to keep our substring continuous.
            if c in substring:
                index = substring.find(c)
                substring = substring[(index + 1)::]
            # Then we are able to add new character to our substring
            # to make sure that there is no duplicated characters and
            # the substring itself is continuous.
            substring += c
            # For every iteration, we compute the length of substring
            length = len(substring)
            # Leave the max value of length for returning
            if length > max_len:
                max_len = length

        return max_len

