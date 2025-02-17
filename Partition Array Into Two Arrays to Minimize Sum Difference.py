# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


def minimizeParitioning(nums):
    
    l = len(nums)
    s = sum(nums)
    dp = [[False for _ in range(s+1)] for _ in range(l+1)]
    
    for i in range(l+1):
        dp[i][0] = True
        
    for i in range(1,l+1):
        for j in range(1,s+1):
            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
                
    arr = []
    
    for i in range(s+1):
        if dp[l][i] == True:
            arr.append(i)
    
    l1 = len(arr)
    l2 = l1//2
    num = s
    for i in arr[:l2]:
        num = min(num, s-2*(i))
        
    return num
        
    
    
nums = [5, 4, 4, 7, 2, 9 ]

print(minimizeParitioning(nums))
    
    
    
    
    
