# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")


def firstNegative(arr, k):
    negativeList = []
    res = []
    i,j = 0,0
    l = len(arr)
    
    while j < l:
        if arr[j] < 0:
            negativeList.append(arr[j])
            
        if j-i+1 < k :
            j += 1
        elif j-i+1 == k:
            
            if len(negativeList): 
                res.append(negativeList[0])
                if arr[i] == negativeList[0]:
                    negativeList.pop(0)
            else:
                res.append(0)
            i += 1
            j += 1
            
    return res
     

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(firstNegative(arr, k))
    
