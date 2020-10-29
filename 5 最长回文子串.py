# _*_coding:utf-8_*_
# @Time    : 2020/10/28 21:46
# https://leetcode-cn.com/problems/longest-palindromic-substring/

s = "babad"
'''
回文串的特点是，去除首尾两端，剩余部分依旧是回文串
在dp表中，i，j位置表示s[i,j+1]串是否是回文串，取决于其左下方s[i+1,j-1]串，即去除首尾的部分是否是回文串
最小子结构：就是子串是否是回文串
循环子问题：遍历所有子串是否满足回文结构，即去掉首尾两端依旧回文，且首尾字符相同
'''
n = len(s)
dp = [[False] * n for _ in range(n)]    # 建n×n的表，dp[i][j]代表s[i:j]是否为回文子串
res = ""        #初始化 最长回文子串
#遍历全部子串，子串起自i，终于j
for Length in range(n): #回文子串长度可取1~n，因此子串跨度0~n-1
    for i in range(n):  #起点为0~n-1
        j = i + Length  #终点为 i + 子串长度Length
        if j >= n:      #若计算的终点超过输入串长度，结束循环
            break
        if Length == 0: #子串跨度为0时，即i=j，单个字符便是回文子串
            dp[i][j] = True #dp表对角线为True
        elif Length == 1:   #子串跨度为1，即子串长度为2
            dp[i][j] = ((s[i] == s[j]))     #若前后相同则为回文子串
        else:       #否则，若子串去除首尾也是回文串，且首为相同，则子串为回文串
            dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
        if dp[i][j] and len(res) < Length + 1:  #若子串s[i,j]是回文串,而且子串长度（跨度+1）> 上一个res回文串
            res = s[i:j+1]      #更新res
print(res)