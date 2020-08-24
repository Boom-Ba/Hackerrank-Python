""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
##Hackerank : Check BST or NOT

def checkBST(root):
    def dfs(root):
        if not root:
            return True, None, None 
        left, left_min, left_max= dfs(root.left)
        right, right_min, right_max= dfs(root.right)
        return  left and right and (not left_max or left_max<root.data) and (not right_min or right_min>root.data),left_min if left_min else root.data,right_max if right_max else root.data
    
    res, min, max= dfs(root)
    return res