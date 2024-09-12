class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        string1 = ''

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])



        i = len1
        j = len2

        while (i > 0 and j > 0):
            if str1[i-1] == str2[j-1]:
                string1 += str1[i-1]
                i -= 1
                j -=1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    string1 += str1[i-1]
                    i -=1
                else:
                    string1 += str2[j-1]
                    j -=1

        while i>0:
            string1 += str1[i-1]
            i -=1
    

        while j >0:
            string1 += str2[j-1]
            j-=1
            
        return string1[::-1]
        
