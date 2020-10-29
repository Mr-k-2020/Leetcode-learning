# _*_coding:utf-8_*_
# @Time    : 2020/10/28 23:02

# https://leetcode-cn.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set_arr = list(set(arr))
        arr_set = list(set(arr))
        arr_count = []
        for i in range(len(arr_set)):
            arr_count.append(arr.count(arr_set[i]))
        before_arr_count = len(arr_count)
        after_arr_count = len(set(arr_count))
        if before_arr_count == after_arr_count:
            return True
        else:
            return False