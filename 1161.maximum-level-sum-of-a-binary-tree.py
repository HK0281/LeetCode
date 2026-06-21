#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        queue.append(root)
        maxsum=float('-inf')
        lvl=0
        maxlvl=0
        while queue:
            size=len(queue)
            sum=0
            for i in range(size):
                node = queue.popleft()
                sum +=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lvl+=1
            if sum>maxsum:
                maxsum=sum
                maxlvl=lvl
        return maxlvl
# @lc code=end

