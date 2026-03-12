# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:        #initial base condition
            return False
        if root.left is None and root.right is None :
            if targetSum == root.val:
                return True
        if root is None and targetSum != 0:
            return False
        
        
        left = self.hasPathSum(root.left,targetSum - root.val)
        
        right = self.hasPathSum(root.right,targetSum - root.val)

        return left or right

        