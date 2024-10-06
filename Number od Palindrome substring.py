# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def find_lps_length(s):
    # initializing a lookup table of dimensions len(s) * len(s)
    
    length = len(s)
    
    dp = [[0 for _ in range(length)] for _ in range(length)]
    
    count = 0
    for i in range(length):
        dp[i][i] = 1
        count +=1 
        
    for start in reversed(range(length)):
        for end in range(start+1, length):
            
            if s[start] == s[end]:
                pLength = end-start+1
                
                if pLength == 2 or pLength -2 == dp[start+1][end-1]:
                    dp[start][end] = pLength
                    count += 1
                else:
                    dp[start][end] = max(dp[start+1][end], dp[start][end-1])
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])
    
    return count
    
s = 'cddpd'
print(find_lps_length(s))
