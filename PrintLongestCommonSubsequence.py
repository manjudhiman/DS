
def printSubsequence(s1,s2,i,j, dp):
    len1 = len(s1)
    len2 = len(s2)
    str1 = ''
    
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
                

    i = len1
    j = len2
   # creating a string: backtrack the dp 
    while (i > 0 and j > 0):
        if s1[i-1] == s2[j-1]:   # if letters match, add  to the string, and go diagonally up. else: find the max from i-1 or j-1
            str1 += s1[i-1]
            i -= 1
            j -=1
        else:
            if dp[i-1][j] > dp[i][j-1]: 
                i -=1
            else:
                j -=1
    return str1[::-1]
   
  

def main():
    s1 ='test1'
    s2 = 'tfe'
    dp =[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    print(printSubsequence(s1,s2,0,0, dp))
    
    
main()
