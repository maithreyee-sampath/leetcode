# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        currLevel = list()
        
        right = list()
        if root is None:
            return []
        currLevel.append(root)
        while currLevel:
            right.append(currLevel[-1].val)
            nextLevel = list()
            for var in currLevel:
                if var.left is not None:
                    nextLevel.append(var.left)
                if var.right is not None:
                    nextLevel.append(var.right)
            currLevel = nextLevel

        return right
