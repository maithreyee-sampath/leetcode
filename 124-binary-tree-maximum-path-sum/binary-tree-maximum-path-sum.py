# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-INF')

        def calMaxSum(node):
            if node is None:
                return 0

            left = max(calMaxSum(node.left),0)
            right = max(calMaxSum(node.right),0)

            self.max_sum = max(self.max_sum,left+right+node.val)
            return max(left,right) + node.val


        calMaxSum(root)
        return self.max_sum