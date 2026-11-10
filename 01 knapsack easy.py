
n = int(input("Enter number of items: "))
profit = list(map(int, input("Enter profits: ").split()))
weight = list(map(int, input("Enter weights: ").split()))
W = int(input("Enter knapsack capacity: "))

# DP table
dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(1, W + 1):
        if weight[i - 1] <= w:
            dp[i][w] = max(
                profit[i - 1] + dp[i - 1][w - weight[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# ---- DP TABLE PRINTING (ONLY CHANGE HERE) ----
print("\nDP Table:")
for row in dp:
    for val in row:
        print(val, end="\t")
    print()

# Final Answer
print("\nMaximum Profit:", dp[n][W])
