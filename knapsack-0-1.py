Approach 1: Recursion

def find_knapsack(capacity, weights, values, n):
    
    def calulateWeights(capacity, weights, values, n):
      if ( n ==0 or capacity == 0):
        return 0
        
      if weights[n-1] <= capacity:
        return max(values[n-1] + calulateWeights(capacity-weights[n-1], weights, values, n-1),
        calulateWeights(capacity, weights,values,n-1))
        
      else:
        return calulateWeights(capacity,weights, values, n-1)
      
      
    return calulateWeights(capacity, weights, values, n) 

Approach 2: DP(top down)

def find_knapsack(capacity, weights, values, n):
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
      for j in range(1,capacity+1):
        if weights[i-1] <= j:
          dp[i][j] = max(values[i-1]+dp[i-1][j-weights[i-1]], dp[i-1][j])
        else:
          dp[i][j] = dp[i-1][j]
          
      
      
    return dp[n][capacity]
