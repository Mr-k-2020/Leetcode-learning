# _*_coding:utf-8_*_
# @Time    : 2020/10/29 15:12

# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

'''
深度优先遍历，递归
'''

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        def DFS(root, tmp):
            if not root:
                return None
            if not root.left and not root.right:
                self.res += int(tmp + str(root.val))
                return self.res
            DFS(root.left, tmp + str(root.val))
            DFS(root.right, tmp + str(root.val))
        DFS(root, '')
        return self.res