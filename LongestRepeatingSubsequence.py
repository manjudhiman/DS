
def printRepeatingSubsequence(s1,s2,i,j, dp):
    len1 = len(s1)
    len2 = len(s2)
    str1 = ''
    
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if s1[i-1] == s2[j-1] and i != j:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[len1][len2]
                
                

def main():
    s1 ='aaaaba'
    
    dp =[[0 for _ in range(len(s1)+1)] for _ in range(len(s1)+1)]
    print(printRepeatingSubsequence(s1,s1,0,0, dp))
    
    
main()
