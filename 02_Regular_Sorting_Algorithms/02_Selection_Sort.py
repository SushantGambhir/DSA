def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index], arr[i] = arr[i], arr[min_index]

arr=[8,1,7,5,2]
selection_sort(arr)
print(arr)

# Complexity Analysis of Selection Sort
# Time Complexity: O(n2) ,as there are two nested loops:

# One loop to select an element of Array one by one = O(n)
# Another loop to compare that element with every other Array element = O(n)
# Therefore overall complexity = O(n) * O(n) = O(n*n) = O(n2)
# Auxiliary Space: O(1) as the only extra memory used is for temporary variables.

# Advantages of Selection Sort
# Easy to understand and implement, making it ideal for teaching basic sorting concepts.
# Requires only a constant O(1) extra memory space.
# It requires less number of swaps (or memory writes) compared to many other standard algorithms. Only cycle sort beats it in terms of memory writes. Therefore it can be simple algorithm choice when memory writes are costly.
# Disadvantages of the Selection Sort
# Selection sort has a time complexity of O(n^2) makes it slower compared to algorithms like Quick Sort or Merge Sort.
# Does not maintain the relative order of equal elements which means it is not stable