# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


def partitionWithDiff(nums, diff):
    t = sum(nums)
    l = len(nums)
    s1 = (t+diff)// 2
    
    dp = [[0 for _ in range(s1+1)] for _ in range(l+1)]
    for i in range(l+1):
        dp[i][0] = 1
        
    for i in range(1,l+1):
        for j in range(s1+1):
            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j-nums[i-1]] +dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[l][s1]
    
    
    
nums = [1,1,2,3]
diff = 1

print(partitionWithDiff(nums,diff))
    
 // Output: 3   
    
    
    
