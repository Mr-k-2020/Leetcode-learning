# _*_coding:utf-8_*_
# @Time    : 2020/10/29 0:32

# https://leetcode-cn.com/problems/string-to-integer-atoi/

'''
使用正则表达式
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)