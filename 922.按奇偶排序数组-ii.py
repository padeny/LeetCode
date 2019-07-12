#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#
# https://leetcode-cn.com/problems/sort-array-by-parity-ii/description/
#
# algorithms
# Easy (64.16%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    12.7K
# Total Submissions: 19.8K
# Testcase Example:  '[4,2,5,7]'
#
# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
#
# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
#
# 你可以返回任何满足上述条件的数组作为答案。
#
#
#
# 示例：
#
# 输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#
#
#
#
# 提示：
#
#
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000
#
#
#
#
#
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        result = [0] * len(A)
        index_odd = 0
        index_even = 1
        for i in A:
            if i % 2 == 0:
                result[index_odd] = i
                index_odd += 2
            else:
                result[index_even] = i
                index_even += 2
        return result

