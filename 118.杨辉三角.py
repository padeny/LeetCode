#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (63.34%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    31.4K
# Total Submissions: 49.5K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(l: list) -> list:
            r = [1]
            for i in range(len(l)-1):
                r.append(l[i]+l[i+1])
            r.append(1)
            return r
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = self.generate(numRows-1)
            res.append(helper(res[-1]))
            return res

