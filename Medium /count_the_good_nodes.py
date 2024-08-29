# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #use depth first search to traverse the tree, and constantly keep track of the current path maximum
        num_good_nodes = 0 
        def dfs(node, max_so_far):
        
            nonlocal num_good_nodes
            if node.val >= max_so_far: 
                num_good_nodes += 1 #because we have already compare the node before with the node before node before, so we only need to compare between the current node with the node before it
            if node.right: 
                dfs(node.right, max(node.val, max_so_far))
            if node.left: 
                dfs(node.left, max(node.val, max_so_far))
        dfs(root, float("-inf")) # the initial max_so_far set to -inf so every node can be greater
        return num_good_nodes

         
            
        