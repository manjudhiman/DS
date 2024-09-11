
#  Total number of chars - Longest Common subsequence

def shortest_common_supersequence(str1, str2):
    # your code will replace the placeholder return statement below
    
    rows = len(str1)
    cols = len(str2)
    
    dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    
    for i in range(1, rows+1):
      for j in range(1, cols+1):
        if str1[i-1] == str2[j-1]:
          dp[i][j] = 1 + dp[i-1][j-1]
        else:
          dp[i][j] = max(dp[i-1][j], dp[i][j-1])
          
    return rows + cols - dp[rows][cols]

'''
Time and space complexityO(m*n)

'''





def shortest_common_supersequence(str1, str2):
    # your code will replace the placeholder return statement below
    
    rows = len(str1)
    cols = len(str2)
    
    dp = [[0 for _ in range(cols+1)] for _ in range(2)]
    
    for i in range(1, rows+1):
      for j in range(1, cols+1):
        dp[i %2][j] =0
        if str1[i-1] == str2[j-1]:
          dp[i%2][j] = 1 + dp[(i-1)%2][j-1]
        else:
          dp[i%2][j] = max(dp[(i-1) %2][j], dp[i%2][j-1])
          
    return rows + cols - dp[rows %2][cols]

'''
Time Complexity O(m*n)
Space Complexity min(O(m,n)
'''
