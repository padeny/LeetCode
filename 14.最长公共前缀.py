#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.92%)
# Likes:    609
# Dislikes: 0
# Total Accepted:    95.2K
# Total Submissions: 280.4K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
# ------------------------------
# 遍历列表，两两从头取交集，内层循环长度为较短的字符串长度，两种情况提前结束：
# 1. 不等于
# 2. cp为""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cp = strs[0] if strs else ""
        for s in strs[1:]:
            f = min(len(cp), len(s))
            cp = cp[:f]

            for i in range(f):
                if s[i] != cp[i]:
                    cp = cp[:i]
                    break
            if not cp:
                return ""
        return cp
