#minimum-maximumusingdivideandconquer
def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    mid = (low + high) // 2
    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid + 1, high)
    return min(min1, min2), max(max1, max2)
arr = []
n = int(input('enter no.of elements: '))
for i in range(n):
  n1 = arr.append(int(input(f'enter element {i+1}: ')))
print(arr)
minimum, maximum = find_min_max(arr, 0, len(arr) - 1)
print(f"Minimum: {minimum}, Maximum: {maximum}")
