# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        #this only gives height of binary tree
        def heightOfTree(node):
            if node is None:
                return 0
            left_height = heightOfTree(node.left)
            right_height = heightOfTree(node.right)
            
            self.diameter = max(self.diameter, left_height + right_height)
            return max(left_height,right_height)+1

        heightOfTree(root)
        return self.diameter
        
        
        

        