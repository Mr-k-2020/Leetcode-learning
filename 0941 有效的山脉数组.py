# _*_coding:utf-8_*_
# @Time    : 2020/11/3 20:57

# https://leetcode-cn.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        left = 0
        right = len(A)-1
        while left < len(A) - 1 and A[left] < A[left+1]:
            left += 1
        while right > 1 and A[right-1] > A[right]:
            right -= 1
        if left > 0 and right < len(A)-1 and left == right:
            return True
        else:
            return False