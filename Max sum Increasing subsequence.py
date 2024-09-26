
def MSIS_Length(nums):
    cal_sum = [i for i in nums]
    cal_len = [i for i in range(0,len(nums))]
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] :
                if (cal_sum[i] < nums[i] + cal_sum[j]):
                    cal_sum[i] = nums[i] + cal_sum[j]
                    cal_len[i] = j
                
    print("cal_len , cal_sum", cal_len, cal_sum) 
    return max(cal_sum)
    
    
    
s = [4, 1, 2, 6, 10, 1, 12]
print(MSIS_Length(s))
