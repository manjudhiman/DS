class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        len1 = len(s)
        len2 = len(t)
        
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        
        
        for i in range(len1):
            dp[i][0] = 1
            
            
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                    
                    
        return dp[len1][len2]        
        
