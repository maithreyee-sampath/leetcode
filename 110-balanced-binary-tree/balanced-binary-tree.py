# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)
            
            return max(left,right)+1


        if root is None:
            return True
        if abs(height(root.left)-height(root.right)) >1:
            return False

        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
            

            

        