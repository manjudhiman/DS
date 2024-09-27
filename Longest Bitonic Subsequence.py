'''
Time complexity : O(n^2)
Space complexity: O(n)
'''
def lbs_length(nums):
    # Write your code here

    # your code will replace the placeholder return statement below
    dp_increasing = [1 for _ in nums]
    dp_decreasing = [1 for _ in nums]
    max_length = 0
    
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp_increasing[i] = max(dp_increasing[i], dp_increasing[j]+1)
                
                
    
    for i in range(len(nums)-1,-1, -1):
        for j in range(i-1, -1,-1):
            if nums[j] > nums[i]:
                dp_decreasing[j] = max(dp_decreasing[j], dp_decreasing[i]+1)
                
    
    for i in range(len(nums)):
        max_length = max(max_length, dp_increasing[i] + dp_decreasing[i] -1)
        
    return max_length
