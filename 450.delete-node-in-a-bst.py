#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        if key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key==root.val:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            replace=root.right
            while replace.left:
                replace=replace.left
        
            root.val=replace.val
            root.right=self.deleteNode(root.right,replace.val)
        return root
# @lc code=end

