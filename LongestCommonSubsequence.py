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
        
        
        
        
        
