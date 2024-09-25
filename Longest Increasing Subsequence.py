'''
Brute Force
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        def helper(i, prev, count):
            if i == len(nums):
                return count
            
            if nums[i] > prev:
                return max(helper(i+1, nums[i], count+1), helper(i+1, prev, count))
            else:
                return helper(i+1, prev, count)
            
        
        return helper(0, - float('inf'), 0)


'''
DP: Time complexity : O(n^2), Space COmplexity: O(n)
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for _ in nums]
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        
        return max(dp)
        
        
                
                
                
                
                
        
            
