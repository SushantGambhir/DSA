def selection_sort(arr):
    n = len(arr)

    for i in range(1,n):
        temp = arr[i]
        j = i-1

        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

arr=[8,1,7,5,2]
selection_sort(arr)
print(arr)

# Time Complexity

# Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
# Average case: O(n2), If the list is randomly ordered
# Worst case: O(n2), If the list is in reverse order
# Space Complexity

# Auxiliary Space: O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.