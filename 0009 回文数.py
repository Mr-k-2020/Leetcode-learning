# _*_coding:utf-8_*_
# @Time    : 2020/10/29 0:50

# https://leetcode-cn.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''方法一：转字符串'''
        # if x < 0:
        #     return False
        # else:
        #     str_x = str(x)
        #     xx = int(str_x[::-1])
        #     if x == xx:
        #         return True
        #     else:
        #         return False
        '''方法二：数学方法'''
        if x < 0: return False
        a, b = x, 0
        while a != 0:
            b = b * 10 + a % 10
            a = a // 10
        return b == x