# _*_coding:utf-8_*_
# @Time    : 2020/11/3 23:46

# https://leetcode-cn.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 3:
            return nums[0] + nums[1] + nums[2]
        d = float('inf')
        nums.sort()
        for i in range(n):
            L = i + 1
            R = n - 1
            while  L < R:
                x = nums[i] + nums[L] + nums[R] - target
                if abs(x) < d:
                    d = abs(x)
                    ans = nums[i] + nums[L] + nums[R]
                if x > 0:
                    R = R - 1
                elif x < 0:
                    L = L + 1
                else:
                    return target
        return ans