# _*_coding:utf-8_*_
# @Time    : 2020/10/29 16:39

# https://leetcode-cn.com/problems/container-with-most-water/

'''
使用双指针，列表首尾各一个指针，比较头尾指针值大小，把小的那个指针向另一个方向移动
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        W_L = []
        while i < j:
            W_L.append(min(height[i], height[j]) * (j-i))
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return max(W_L)