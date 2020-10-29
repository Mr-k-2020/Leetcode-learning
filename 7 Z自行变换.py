# _*_coding:utf-8_*_
# @Time    : 2020/10/28 23:26

# https://leetcode-cn.com/problems/zigzag-conversion/
'''
找规律以 n = numRows * 2 - 2 为一个循环，字符所在行号 min(i % n, n - i % n)
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            n = numRows * 2 - 2
            rows = [""] * numRows
            for i, char in enumerate(s):
                rows[min(i % n, n - i % n)] += char
            return "".join(rows)