"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.postorder_traversal_list = []

    def extract_val(self, root: TreeNode | None):
        if not root:
            return

        self.extract_val(root.left)
        self.extract_val(root.right)
        self.postorder_traversal_list.append(root.val)

    def postorderTraversal(self, root: TreeNode | None = None) -> list[int]:
        self.extract_val(root)
        return self.postorder_traversal_list
