def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        flag = True
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                flag = False
                arr[j], arr[j+1] = arr[j+1],arr[j]
        if flag:
            break

arr=[8,1,7,5,2]
bubble_sort(arr)
print(arr)

# The best case complexity reduces to the order of n, but the worst and average is still n2. 
# So, overall the complexity is of the order of n2 again.