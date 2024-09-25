'''
Time complexity: O(n^2)
Space complexity: O(n)
'''

def min_deletions(nums):

    dp = [1 for _ in nums]
    
    for i in range(1, len(nums)):
      for j in range(i):
        if nums[i] > nums[j]:
          dp[i] = max(dp[i], dp[j]+1)
          
          
    lis = max(dp)
    
    return len(nums)-lis
