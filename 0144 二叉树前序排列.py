# _*_coding:utf-8_*_
# @Time    : 2020/10/27 23:05

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        L = []  #新建列表，用于返回
        def pre_order(root):    #定义新函数
            if root:            #如果有根节点
                L.append(root.val)  #L自增根节点值
                pre_order(root.left)    #递归
                pre_order(root.right)   #递归
        pre_order(root)     #执行新函数，参数为给定的根节点
        return L