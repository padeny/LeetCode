#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (51.58%)
# Likes:    277
# Dislikes: 0
# Total Accepted:    40.3K
# Total Submissions: 78.1K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
#
# 注意：整数顺序将表示为一个字符串。
#
#
#
# 示例 1:
#
# 输入: 1
# 输出: "1"
#
#
# 示例 2:
#
# 输入: 4
# 输出: "1211"
#
#
#
class Solution:
    def inner(self, s):
        res = []
        i = j = 0
        while j < len(s):
            if s[i] != s[j]:
                res.extend([str(j-i), s[i]])
                i = j
            j += 1
        res.extend([str(j-i), s[i]])
        return ''.join(res)

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        return self.inner(self.countAndSay(n-1))
