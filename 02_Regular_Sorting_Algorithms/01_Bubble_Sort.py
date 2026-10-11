def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]

arr=[8,1,7,5,2]
bubble_sort(arr)
print(arr)

# Complexity Analysis of Bubble Sort:
# Time Complexity: O(n2)
# Auxiliary Space: O(1)

# Advantages of Bubble Sort
# Bubble sort is easy to understand and implement.
# It does not require any additional memory space.
# It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.
# Disadvantages of Bubble Sort
# Bubble sort has a time complexity of O(n2) which makes it very slow for large data sets.
# Bubble sort has almost no or limited real world applications. It is mostly used in academics to teach different ways of sorting.