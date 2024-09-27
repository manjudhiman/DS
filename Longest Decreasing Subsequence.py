def LDS(nums):
    dp = [1 for _ in nums]
    
    for i in range(len(nums)-1,-1,-1):
        for j in range(i-1,-1,-1):
            print("++i j ", i,j, dp)
            if nums[i] < nums[j]:
                dp[j] =  max(dp[j],dp[i]+1)
                
                
    return max(dp)
    
    
    
    
    

s =  [50, 3, 10, 7, 40, 80]
print(LDS(s))
