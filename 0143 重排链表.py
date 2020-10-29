# _*_coding:utf-8_*_
# @Time    : 2020/10/21 10:47

# https://leetcode-cn.com/problems/reorder-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        # 用快慢指针把链表一分为二，前半部分长度 >= 后半部分长度
        # first 为前半部分的头部，second 为后半部分的头部
        first = low = fast = head
        while fast.next and fast.next.next:
            fast, low = fast.next.next, low.next
        # 断开两个链，一个是前半部分与后半部分断开，一个是后半部分的头与后面的断开，所以有两个None
        second, node, low.next, second.next = low.next, low.next.next, None, None
        # 后半部分逆序
        while node:
            node.next, second, node = second, node, node.next
        # 前后部分交替链接
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next