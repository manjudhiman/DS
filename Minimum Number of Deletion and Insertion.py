def min_del_ins(str1, str2):

    # write your code here
    
    len1 = len(str1)
    len2 = len(str2)
    
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    
    lcs = 0
    for i in range(1, len1+1):
      for j in range(1, len2+1):
        if str1[i-1] == str2[j-1]:
          dp[i][j] = 1 + dp[i-1][j-1]
        else:
          dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs = dp[len1][len2]
    return [len1-lcs, len2-lcs]



'''
Time and Space Complexity: O(m*n)
