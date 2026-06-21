#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue=deque()
        queue.append(root)
        if queue is None:
            return None
        while queue:
            node = queue.popleft()
            if node.val==val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
# @lc code=end

