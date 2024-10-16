#User function Template for python3  Time COmplexity O(n^3), Space O(n^2)

#Implentation using map

class Solution:
    
    def countWays(self, n, s):
        res = {}
        
        # code here
        def findWays(string, i, j, isTrue):
            if i > j:
                return 0
                
            if i == j:
                if isTrue == 1:
                    return 1 if string[i] == 'T' else 0
                else:
                    return 1 if string[i] == 'F' else 0
        
            if (i,j,isTrue) in res:
                return res[(i,j,isTrue)]
            else: 
                ans = 0       
                for k in range(i+1, j,2):
                   
                    leftT = findWays(string,i,k-1, 1)
                    leftF = findWays(string,i,k-1,0)
                    rightT = findWays(string,k+1,j,1)
                    rightF = findWays(string,k+1,j,0)
                    if string[k] == '&':
                        if isTrue == 1:
                            ans += leftT * rightT
                        else:
                            ans += leftT*rightF + leftF*rightT + leftF*rightF
                            
                    elif string[k] == '|':
                        if isTrue == 1:
                            ans += leftT*rightF + leftF*rightT + leftT*rightT
                        else:
                            ans += leftF*rightF
                    elif string[k] == '^':
                        if isTrue == 1:
                            ans += leftT*rightF + leftF*rightT
                        else:
                            ans += leftT*rightT + leftF*rightF
        
                res[(i,j,isTrue)] = ans
            return  res[(i,j,isTrue)]
        
        
        return findWays(s, 0, n-1, 1)
    
        
        
        
  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends





#############


#User function Template for python3 USNG DP
Time complexity : O(n^2)
Space complexity: O(n^2)

class Solution:
    
    def countWays(self, n, s):
        dp  = [[[-1 for _ in range(2)] for _ in range(n+1)] for _ in range(n+1)]
        
        
        # code here
        def findWays(string, i, j, isTrue):
          
            if i > j:
                return 0
                
            if i == j:
                if isTrue == 1:
                    return 1 if string[i] == 'T' else 0
                else:
                    return 1 if string[i] == 'F' else 0
        
        
            if dp[i][j][isTrue] != -1:
                return dp[i][j][isTrue]
        
            else: 
                ans = 0       
                for k in range(i+1, j,2):
                    if dp[i][k-1][1] != -1:
                        leftT = dp[i][k-1][1]
                    else:
                        leftT = findWays(string,i,k-1, 1)
                    
                    if dp[i][k-1][0] != -1:
                        leftF = dp[i][k-1][0]
                    else:
                        leftF = findWays(string,i,k-1,0)
                    
                    if dp[k+1][j][1] != -1:
                        rightT = dp[k+1][j][1]
                    else:
                        rightT = findWays(string,k+1,j,1)
                        
                    if dp[k+1][j][0] != -1:
                        rightF = dp[k+1][j][0]
                    else:
                        rightF = findWays(string,k+1,j,0)
                        
                        
                    if string[k] == '&':
                        if isTrue == 1:
                            ans += leftT * rightT
                        else:
                            ans += leftT*rightF + leftF*rightT + leftF*rightF
                            
                    elif string[k] == '|':
                        if isTrue == 1:
                            ans += leftT*rightF + leftF*rightT + leftT*rightT
                        else:
                            ans += leftF*rightF
                    elif string[k] == '^':
                        if isTrue == 1:
                            ans += leftT*rightF + leftF*rightT
                        else:
                            ans += leftT*rightT + leftF*rightF
        
                dp[i][j][isTrue] = ans
            return  ans
        
        
        return findWays(s, 0, n-1, 1)
    
        
        
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends
