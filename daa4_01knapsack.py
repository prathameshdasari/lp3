def knapsack_dp(profits, weights, capacity):
    n = len(profits)

    print("Profits:", profits)
    print("Weights:", weights)
    print("Capacity:", capacity)

    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


capacity = int(input("Enter the knapsack capacity: "))
n = int(input("Enter the number of items: "))

profits = []
weights = []

for i in range(n):
    profit = int(input(f"Enter profit for item {i+1}: "))
    weight = int(input(f"Enter weight for item {i+1}: "))
    profits.append(profit)
    weights.append(weight)

    
max_profit = knapsack_dp(profits, weights, capacity)
print(f"The maximum profit the knapsack can hold is: {max_profit}")


# DP for optimization problem
# solved in sequence of decisions
# try all possible solutions and pickup the best one
# dp = 1. optimal substrctures, 2. overlapping subproblems
# same solution stored once and used repetedly without solving again and again
# thats main difference b/w divide and conqure and DP


# ex:
# capacity = 8
# profits  = [1,2,5,6]
# weights  = [2,3,4,5]

#              capacity
#          0 1 2 3 4 5 6 7 8
# p  w  0  0 0 0 0 0 0 0 0 0  
# 1  2  1  0 0 1 1 1 1 1 1 1 
# 2  3  2  0 0 1 2 2 3 3 3 3
# 5  4  3  0 0 1 2 5 5 6 7 7
# 6  5  4  0 0 1 2 5 6 6 7 8