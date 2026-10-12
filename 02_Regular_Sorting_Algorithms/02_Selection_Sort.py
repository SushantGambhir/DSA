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