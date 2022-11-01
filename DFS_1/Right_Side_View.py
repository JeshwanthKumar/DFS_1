# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: Recursive stack space - O(n)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []    #Initialize result as an empty array
        self.dfs(root, 0)   #Recursize function call
        return self.result  #Return result
        
    def dfs(self, root, height):    #Recursive function with root and a height variable to calc the level
        #base condition
        if root == None:    #If the root is None then return which unfolds the recursion
            return
        
        if height >= len(self.result):  #If the height is greater than or equal to lenght of the result append the root.val into the result
            self.result.append(root.val)
        
        self.dfs(root.right, height+1)  #Recursive call for the right side of the tree and increment height by 1
        self.dfs(root.left, height+1)   #Recursive call for the left side of the tree and increment height by 1