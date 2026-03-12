# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        q = deque()
        q.append(root)
        if root is None:
            return 0
        while q:
            node = q.popleft()
            count+=1
            if node.left is not None and node.right is not None:
                q.append(node.left)
                q.append(node.right)
            elif node.left is None and node.right is not None:
                return 0
            elif node.left is not None and node.right is None:
                    q.append(node.left)
        return count

        
