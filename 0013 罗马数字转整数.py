# _*_coding:utf-8_*_
# @Time    : 2020/10/29 17:16

# https://leetcode-cn.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        adict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
                 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        alist = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        s = s + ' '
        res, i = 0, 0
        while i < len(s)-1:
            if s[i]+s[i+1] in alist:
                res = res + adict[s[i]+s[i+1]]
                i = i + 2
            else:
                res = res + adict[s[i]]
                i = i + 1
        return res