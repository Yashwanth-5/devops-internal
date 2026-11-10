# 0/1Knapsack
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    print("\nDP Table:")
    for row in dp:
        print("\t".join(str(x) for x in row))
    return dp[n][W]
n = int(input("Enter number of items: "))
weights = []
values = []
print("Enter weight and value for each item:")
for i in range(n):
    w = int(input(f"Weight of item {i+1}: "))
    v = int(input(f"Value of item {i+1}: "))
    weights.append(w)
    values.append(v)
capacity = int(input("Enter knapsack capacity: "))
max_value = knapsack(weights, values, capacity)
print("\nMaximum value:", max_value)
