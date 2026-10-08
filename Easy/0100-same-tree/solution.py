# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # If both nodes are None, they are identical.
        if not p and not q:
            return True
        # If only one of them is None, they are not identical.
        if not p or not q:
            return False
        # If values match, recursively check left and right subtrees.
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))