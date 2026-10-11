def search(arr,x):
    n = len(arr)

    for i in range(n):
        if arr[i]==x:
            return i
    return -1

arr = [5,10,15,20,25,30,35,40,45,50,55,60]

index = search(arr,15)

if(index==-1):
    print('Not found')
else:
    print(f'Number present at index {index}')

# Time Complexity:
# Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
# Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.
# Average Case: O(N)
# Auxiliary Space: O(1) as except for the variable to iterate through the list, no other variable is used. 