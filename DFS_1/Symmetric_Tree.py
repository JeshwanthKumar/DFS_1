# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: Recursive stack space- O(n)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #Base condition
        if not root:    #If there is no root return False 
            return False
        
        return self.dfs(root.left, root.right)  #Recursive function call

    def dfs(self, left, right): #Recursive function with left and right
        #base condition
        if left == None and right == None:  #If there is no left and right then return True which means the end of the tree
            return True
        
        if left == None or right == None:   #If either left or right is None return False
            return False
        
        if left.val != right.val:   #If the value of left is not equal to the value of right then return False
            return False
        

        return self.dfs(left.right, right.left) and self.dfs(left.left, right.right)    #Return if the recursive call satisfies all the condition
        