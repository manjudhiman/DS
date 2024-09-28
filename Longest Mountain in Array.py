class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        '''
        Space complexity : O(n)
        '''
        length = len(arr)
        if length < 3:
            return 0
        
        res = 0
        for i in range(1, length-1):
            if arr[i]> arr[i-1] and arr[i] > arr[i+1]:
                count = 1
                j = i
                while j > 0 and arr[j] > arr[j-1]:
                    j -= 1
                    count += 1
                k = i
                while k < length-1 and  arr[k] > arr[k+1]:
                    k += 1
                    count += 1
                    
                res = max(res, count)
            
                
        return res
                
                
                
                
        
        
        
        '''
        length = len(arr)
        
        if length < 3:
            return 0
        
        inc_dp = [ 1 for _ in arr]
        dec_dp = [ 1 for _ in arr]
        
        
        for i in range(1,length):
            if arr[i] > arr[i-1]:
                inc_dp[i] = max(inc_dp[i], inc_dp[i-1]+1)

        
        for i in range(length-2,-1,-1):
            if arr[i] > arr[i+1]:
                dec_dp[i] = max(dec_dp[i],dec_dp[i+1]+1)
                    
                    
        max_len = 0
        
        for i in range(1,length-1):
            if inc_dp[i] > 1 and dec_dp[i] > 1:
                max_len = max(max_len, inc_dp[i] + dec_dp[i]-1)
                
                
        return max_len
                
       '''
        
