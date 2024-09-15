#Top down  Time complexity: O(m*n)
#Space ComplexityL O(m*n)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        cache = {}
     
        def calInterLeaveFunction(s1,s2,s3, i1,i2,i3):
            if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
                return True
            
            if i3 == len(s3):
                return False
            
            
            if (i1,i2,i3) in cache:
                return cache[i1,i2,i3]
            
            d1 = False
            d2 = False
            if i1 < len(s1):
                if s1[i1] == s3[i3]:
                    d1 = calInterLeaveFunction(s1,s2,s3,i1+1,i2,i3+1)
                    
                
            if i2 < len(s2):
                if s2[i2] == s3[i3]:
                    d2 = calInterLeaveFunction(s1,s2,s3,i1,i2+1,i3+1)
            
            cache[i1,i2,i3] = d1 or d2
            return cache[i1,i2,i3]
        
        return calInterLeaveFunction(s1,s2,s3,0,0,0)
            
            
        
        
        
