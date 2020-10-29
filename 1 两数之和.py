# _*_coding:utf-8_*_
# @Time    : 2020/10/29 0:53

# https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]