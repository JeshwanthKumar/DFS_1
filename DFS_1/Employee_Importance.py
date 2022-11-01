"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
#Time_Complexity: O(n)
#Space_Complexity: Recursive stack - O(n)



class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.totalImportance = 0    #Initialize totalImportance as 0
        self.adj = {}   #Initailze adjacency matrix
        
        for emp in employees:   #For every employees
            self.adj[emp.id]  = [emp.importance, emp.subordinates]  #Add importance and the subordinates of employees by their id
            
        self.dfs(id)    #Recursive call function
        
        return self.totalImportance #Retrun totalImportance
        
    def dfs(self, employee):    #REcursive function with employee
        self.totalImportance += self.adj[employee][0]   #Add totalImportance with importance of the employee in the adjacency matrix 
        
        for subordinate in self.adj[employee][1]:   #For every subordinate in the adjacency matrix
            self.dfs(subordinate)   #Recursive call for the subordinate
            
        return  #Return unfolds the recursion