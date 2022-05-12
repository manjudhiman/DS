from turtle import down


Problem Statement#
Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

Example 1:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: The longest common substring is "bd".
Example 2:

Input: s1 = "passport"
       s2 = "ppsspt"
Output: 3
Explanation: The longest common substring is "ssp".


Solution 1: Brute Force


```
    def find_LCS_length(s1, s2):
    # TODO: Write your code here
    return findLCS(s1, s2, 0,0,0)

    def findLCS(s1, s2, i,j, count):
        if len(s1) <= i or len(s2) <= j:
            return count
        
        if s1[i] == s2[j]:
            count = findLCS(s1, s2, i+1, j+1, count+1)
    
    
        c1 = findLCS(s1, s2, i+1, j, 0)
        c2 = findLCS(s1, s2, i, j+1, 0)
        
        return max(max(c1, c2), count)

    def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))
    
    main()


  Because of the three recursive calls, the time complexity of the above algorithm is exponential O(3^{m+n})
O(3 
m+n
 )
, where ‘m’ and ‘n’ are the lengths of the two input strings. The space complexity is O(m+n)
O(m+n)
, this space will be used to store the recursion stack.
````


Solution 2 : Top down Approach

````
def find_LCS_length(s1, s2):
  # TODO: Write your code here
  
  n1, n2 = len(s1), len(s2)
  maxLen = min(n1, n2)  # Max possible common length
  
  dp = [[[-1 for _ in range(maxLen)] for _ in range(n2)] for _ in range(n1)]
  return findLCS(dp, s1, s2, 0,0,0)

def findLCS(dp, s1, s2, i,j, count):
    if len(s1) <= i or len(s2) <= j:
        return count
    
    if dp[i][j][count] == -1:
        c3 = count
        if s1[i] == s2[j]:
            c3 = findLCS(dp, s1, s2, i+1, j+1, count+1)
      
       
        c1 = findLCS(dp, s1, s2, i+1, j, 0)
        c2 = findLCS(dp, s1, s2, i, j+1, 0)
        
        dp[i][j][count] = max(max(c1, c2), c3)
    
    return dp[i][j][count]

def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))
  
main()
````


Solution 3: Bottom up Approach

````
def find_LCS_length(s1, s2):
  # TODO: Write your code here
  
  n1, n2 = len(s1), len(s2)
  
  dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
  
  maxLen = 0
  for i in range(1, n1+1):
      for j in range(1, n2+1):
          
          if s1[i-1] == s2[j-1]:
              dp[i][j] = 1 + dp[i-1][j-1]
              maxLen = max(maxLen, dp[i][j])
              
  return maxLen
  

def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))

  
main()

The time and space complexity of the above algorithm is O(m*n)
O(m∗n)
, where ‘m’ and ‘n’ are the lengths of the two input strings.
````



````
Solution with O(n) space complexity

def find_LCS_length(s1, s2):
  # TODO: Write your code here
  n1, n2 = len(s1), len(s2)
  dp = [[0 for _ in range(n2+1)] for _ in range(2)]
  maxLength = 0
  for i in range(1, n1+1):
   
    for j in range(1, n2+1):
      dp[i % 2][j] = 0
      if s1[i - 1] == s2[j - 1]:
        dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
        maxLength = max(maxLength, dp[i % 2][j])
       

  return maxLength
  

def main():
  print(find_LCS_length("abdca", "cbda"))
  '''
  print(find_LCS_length("passport", "ppsspt"))
  '''

  
main()
````