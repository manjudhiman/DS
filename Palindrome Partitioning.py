Approach 1: DFS
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s, [], result)
        return result

    
    def isPalindrome(self, s):
        return s == s[::-1]

    def dfs(self, s,path, result):
        if not s:
            result.append(path)
            return

        for i in range(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:],path+[s[:i]], result)


Approach 2: DFS + DP

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        result = []
        dp = [[ False for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dp[i][i] = True

        for i in reversed(range(N-1)):
            for j in range(i,N):
                if s[i] == s[j]:

                    pLength = j-i+1
                    if pLength == 2 or  dp[i+1][j-1]:
                        dp[i][j] = True

        
        def dfs(start, path):
            if start == N:
                result.append(path)
                return
            
            for i in range(start,N):
                if dp[start][i]:
                    dfs(i+1,path + [s[start:i+1]])
        dfs(0,[])

        return result


        
        


        
