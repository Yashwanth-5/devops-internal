#fractionalknapsack
def fractional_knapsack(values, weights, capacity):
    items = [(v/w, w, v) for v, w in zip(values, weights)]
    items.sort(key=lambda x: x[0], reverse=True)
    total_value = 0
    for value_per_weight, weight, value in items:
        if capacity == 0:
            break
        if weight <= capacity:
            capacity -= weight
            total_value += value
        else:
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0
    return total_value
n = int(input("Enter number of items: "))
values = []
weights = []
for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)
capacity = float(input("Enter capacity of knapsack: "))
optimal_profit = fractional_knapsack(values, weights, capacity)
print(f"Maximum profit (optimal value): {optimal_profit}")
