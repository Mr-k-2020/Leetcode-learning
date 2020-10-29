# _*_coding:utf-8_*_
# @Time    : 2020/10/29 18:11

# https://leetcode-cn.com/problems/longest-common-prefix/

# 学习zip(*item)和zip(item[0],item[1])
#zip是返回元组的迭代器，元组中包含元组中相同索引位置上的值组成的索引

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                s = s + i[0]
            else:
                break
        return s
