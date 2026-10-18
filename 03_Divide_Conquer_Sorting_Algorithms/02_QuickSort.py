def quick_sort(arr,low,high):
    if low >= high:
            return
 
    pivotIndex = partitionArray(arr, low, high)
    quick_sort(arr, low, pivotIndex - 1)
    quick_sort(arr, pivotIndex + 1, high)

def partitionArray(arr, low, high):
        pivot = arr[high]
        smallerIndex = low - 1
 
        for current in range(low, high):
            if arr[current] <= pivot:
                smallerIndex += 1
                arr[smallerIndex], arr[current] = arr[current], arr[smallerIndex]
 
        arr[smallerIndex + 1], arr[high] = arr[high], arr[smallerIndex + 1]
        return smallerIndex + 1

arr=[8,1,7,5,2]
quick_sort(arr,0,len(arr)-1)
print(arr)

# Time Complexity:

# Best Case: (Ω(n log n)), Occurs when the pivot element divides the array into two equal halves.
# Average Case (θ(n log n)), On average, the pivot divides the array into two parts, but not necessarily equal.
# Worst Case: (O(n²)), Occurs when the smallest or largest element is always chosen as the pivot (e.g., sorted arrays).
# Auxiliary Space:

# Worst-case scenario: O(n) due to unbalanced partitioning leading to a skewed recursion tree requiring a call stack of size O(n).
# Best-case scenario: O(log n) as a result of balanced partitioning leading to a balanced recursion tree with a call stack of size O(log n).