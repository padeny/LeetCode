#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.81%)
# Likes:    902
# Dislikes: 0
# Total Accepted:    92.3K
# Total Submissions: 238K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
# ----------------------------
# 栈
class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "[": "]", "{": "}"}
        if not s:
            return True
        l = []
        f = len(s) // 2
        for char in s:
            if char in d.keys():
                l.append(char)
            elif not l or d[l.pop()] != char:
                return False
            if len(l) > f:
                return False
        return not bool(l)
