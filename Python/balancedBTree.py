Balanced Binary Tree
Problem Statement: We are given a binary tree we need to determine whether the given tree is Balanced Binary Tree or not.

A balanced binary tree is a binary tree that follows the 3 conditions: The height of the left and right tree for any node does not differ by more than 1.

Code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root):
            height = 0
            if root is None:
                return 0

            lh = maxDepth(root.left)
            if lh == -1: return -1
            rh = maxDepth(root.right)
            if rh == -1: return -1
            if abs(lh - rh) > 1: return -1
            height = 1 + max(lh, rh)
            return height


        return maxDepth(root) != -1
