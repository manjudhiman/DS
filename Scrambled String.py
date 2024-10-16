class Solution:
  
        
    def isScramble(self, s1: str, s2: str) -> bool:
        
        len1 = len(s1)
        len2 = len(s2)
        
        if len1 != len2:
            return False
        
        if len1 == 0 and len2 == 0:
            return True
        
        scrambleMap= {}
        
        def solve(s1, s2):
              
            if (s1,s2) in scrambleMap:
                return scrambleMap[(s1,s2)]
            
            # check if both have same all characters if not return False
            if not sorted(s1) == sorted(s2): 
                return False
            
            # if both strings are same return True
            if (s1 == s2):
                return True
          
            
            length = len(s1)
            if length < 1:
                return False
            ans = False
            
            for k in range(1, length):
                c1 = solve(s1[0:k], s2[length-k:])
                c2 = solve(s1[k:], s2[0:length-k])
                c3 = solve(s1[0:k], s2[0:k])
                c4 = solve(s1[k:], s2[k:])
                
                
                cond1 = c1 and c2
                cond2 = c3 and c4
              
                if (cond1 or cond2):
                    ans = True
                    scrambleMap[(s1,s2)] = ans
                    break
                else:
                    scrambleMap[(s1,s2)] = ans
                
            
            
            return ans
                
            
        
        return solve(s1,s2)
        
        
        
        
        
        
        
        
        
        
        
        
        
