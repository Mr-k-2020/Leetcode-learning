# _*_coding:utf-8_*_
# @Time    : 2020/10/24 15:22

#方法一
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = []
        for i in range(n):
            N = 0
            for j in range(i+1):
                N = N + nums[j]
            L.append(N)
        return L

#方法二
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newnums = nums
        for i in range(1, len(nums)):
            newnums[i] = newnums[i-1] + newnums[i]
        return newnums