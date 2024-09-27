def LDS(nums):
    length = len(nums)
    dp = [1 for _ in nums]
    
    for i in range(length-2,-1, -1):
        for j in range(i,length):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] +1)
                
                
    return max(dp)
                



s =  [50, 3, 10, 7, 40, 80]
print(LDS(s))
