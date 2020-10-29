# _*_coding:utf-8_*_
# @Time    : 2020/10/28 23:58

# https://leetcode-cn.com/problems/reverse-integer/

class Solution:
    def reverse(self, x:int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != '-':
            x = int(str_x[::-1])        #全部翻转,包括首位
        else:
            x = -int(str_x[:0:-1])      #末尾到首位之前翻转，不包括首位
        return x if -2**31 < x < 2**31-1 else 0