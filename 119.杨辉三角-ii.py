#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (57.26%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    20K
# Total Submissions: 34.9K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(l: list) -> list:
            r = [1]
            for i in range(len(l)-1):
                r.append(l[i]+l[i+1])
            r.append(1)
            return r
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            res = self.getRow(rowIndex-1)
            cur = helper(res)
            return cur

