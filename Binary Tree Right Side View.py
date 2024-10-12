# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
       
        '''
        #REcursive: O(n)
        '''
        res = []
        
        def rightView(node, depth):
            
            if not node:
                return None
            
            if depth == len(res):
                res.append(node.val)
                
            if node.right:
                rightView(node.right, depth+1)
            if node.left:
                rightView(node.left, depth+1)
          
        
        rightView(root, 0)
        
        return res


'''
Iterative approach, O(n)

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        nextLevel = [root] if root else []
        
        while nextLevel:
            res.append(nextLevel[-1].val)
            
            temp, nextLevel = nextLevel, []
            
            for i in temp:
                if i.left:
                    nextLevel.append(i.left)
                
                if i.right:
                    nextLevel.append(i.right)
        
        return res
                    
            
                
        
        
        
  
                
        
        
        
