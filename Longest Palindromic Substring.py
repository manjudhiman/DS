class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        length = len(s)
        
      
        
        dp = [[0 for _ in range(length)] for _ in range(length)]
        
        for i in range(length):
            dp[i][i] = 1
            
        
        palindrome = s[0]
     
        for start in reversed(range(length)):
            for end in range(start+1, length):
                
                if s[start] == s[end]:
                    pLength = end-start+1
                    
                    if pLength == 2 or pLength-2 == dp[start+1][end-1]:
                        dp[start][end] = pLength
                        
                        if pLength > len(palindrome):
                            palindrome = s[start:end+1]
                            
                    else:
                        dp[start][end] = max(dp[start+1][end], dp[start][end-1])
                        
                else:
                    dp[start][end] = max(dp[start+1][end], dp[start][end-1])
        

        return palindrome
                        
                    
