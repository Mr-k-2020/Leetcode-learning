# _*_coding:utf-8_*_
# @Time    : 2020/10/28 0:55

# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

# res初始化为0，建立两个索引i和j，判断新来的字符，是否在s[i:j]中出现
# 若没有出现，更新res，取之前res与i到j的最大值
# 若出现了，则更新i索引
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = i = 0
        for j in range(len(s)):     #建立两个索引i和j，判断新来的字符，是否在s[i:j]中出现
            if s[j] not in s[i:j]:  # 若没有出现
                res = max(res, j+1-i)   # 更新res，取之前res与i到j的最大值
            else:   # 若出现了
                i = i + s[i:j].index(s[j]) + 1  #更新i的位置
        return res