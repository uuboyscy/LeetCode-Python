"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.preorder_traversal_list = []

    def extract_val(self, root: TreeNode | None = None) -> TreeNode | None:
        if not root:
            return

        self.preorder_traversal_list.append(root.val)
        self.extract_val(root.left)
        self.extract_val(root.right)

    def preorderTraversal(self, root: TreeNode | None = None) -> list[int]:
        self.extract_val(root)
        return self.preorder_traversal_list
