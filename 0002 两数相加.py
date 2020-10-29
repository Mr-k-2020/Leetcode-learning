# _*_coding:utf-8_*_
# @Time    : 2020/10/27 23:31

# https://leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
本题需考虑另外两种情况
1，2，3 + 1，2，3，4，5，6 即两个链表长度不同，短的链表补0
1，1 + 9，9 = 110 即有进位的情况
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new = p = ListNode(0)   #创建新链表，新链表初始值为0，指针为None，new和p指针指向新链表头节点
        s = 0   #初始化s表示进位值
        while l1 or l2 or s:    #当l1，l2或s有一个存在，就执行
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + s   #进位值s表示对应位置相加 + 之前的进位
            p.next = ListNode(s % 10)   #新建节点，值为s对10取余，用于抽取进位，用p.next指针指向
            p = p.next  #移动指针P
            s = s // 10 #s对10整除，获取进位
            l1 = l1.next if l1 else 0   #判断长短链表，链表短了就自动补0
            l2 = l2.next if l2 else 0   #同上
        return new.next #返回新链表头指针的下一个节点，因为new指针指向的是新链表的开头为0的初始节点