class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)+1
        dp = [False]*l
        
        dp[0] = True
        
        for i in range(1, l):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                    
        return dp[-1]
