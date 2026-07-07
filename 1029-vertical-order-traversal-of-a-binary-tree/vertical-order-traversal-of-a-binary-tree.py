# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = deque([(root, 0, 0)]) #node, row, col value stored as a tuple
        cols = defaultdict(list) # to store vals like 0: [1,2,3] 

        min_col, max_col = 0, 0
        while q:
            node, row, col = q.popleft()
            min_col, max_col = min(min_col, col), max(max_col, col)
            cols[col].append((row, node.val))

            if node.left:
                q.append((node.left, row + 1,  col - 1)) #passing the val in a tuple form
            if node.right:
                q.append((node.right, row + 1, col + 1))

        res = []
        for c in range(min_col, max_col+ 1):
            sorted_cols = sorted(cols[c])
            res.append([val for row, val in sorted_cols])

        return res


        