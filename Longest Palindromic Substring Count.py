

#Time  Complexity : O(n^2)
#Space Complexity : O(n^2)
def find_lps_length(s):
    # initializing a lookup table of dimensions len(s) * len(s)
    length = len(s)
    dp = [[0 for _ in range(length)] for _ in range(length)]
    
    for i in range(length):
        dp[i][i] = 1
    
    for start in reversed(range(length)):
        for end in range(start+1, length):
            if s[start] == s[end]:
                pLength = end-start+1
                
                
                # to check if the substring is also palindrome or if length is 2
                if pLength == 2 or pLength -2 == dp[start+1][end-1]:
                    dp[start][end] = pLength
                    
                else:
                    dp[start][end] = max(dp[start+1][end], dp[start][end-1])
                
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])
    
    
   
    return dp[0][length-1]
s = 'abcbq'
print(find_lps_length(s))
