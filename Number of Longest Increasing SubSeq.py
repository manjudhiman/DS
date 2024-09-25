class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        length = [1 for _ in nums]
        count = [1 for _ in nums]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j]+1 > length[i]:
                        length[i], count[i] = length[j]+1, count[j]
                        
                    elif length[j]+1 == length[i]:
                        count[i]+= count[j]
                        
                        
        max_length = max(length)
        
        return sum(max_c for max_c,max_l in zip(count, length) if max_l == max_length)
