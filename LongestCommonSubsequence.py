#Top Down approach, Time complexity and space Complexity :(m*n) 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        
        
        
        
        def findLongestSubsequence(text1, text2, i,j, dp):
            
            if i == len(text1) or j == len(text2):
                return 0
            
            if dp[i][j] != 0:
                return dp[i][j]
            
            if text1[i] == text2[j]:
                dp[i][j] = 1 + findLongestSubsequence(text1, text2, i+1,j+1, dp)
                
            else:
                dp[i][j] = max(findLongestSubsequence(text1, text2, i+1,j, dp), findLongestSubsequence(text1,text2,i,j+1, dp))
                
            return dp[i][j]
        
        return findLongestSubsequence(text1, text2,0,0, dp)



#Bottom Up Time and space complexity O(m*n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        
        
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[rows][cols]
        
        
    
        
        
        
        
        
    
  
