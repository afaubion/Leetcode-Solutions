# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(root):
            if root is None:
                return 0
            elif root.val >= L and root.val <= R: #if our current value is between the boundaries, other values could be on the left or right
                return (dfs(root.left) + root.val + dfs(root.right))
            elif root.val >= L: #when our value is >= L, but not <= R, then values are just in left subtree
                return dfs(root.left)
            elif root.val <= R: #when our value is <= R, but not >= L, then values just in right subtree
                return dfs(root.right)
            else:
                return 0
        return dfs(root)