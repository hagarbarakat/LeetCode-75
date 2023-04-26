"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        def preorderTraversal(arr, root): 
            if root: 
                arr.append(root.val)
                for node in root.children: 
                    preorderTraversal(arr, node)
            return arr
        return preorderTraversal(arr, root)