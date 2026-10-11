# Applicable only for sorted array

def search(arr,x,l,h):

    mid = l + (h-l)//2

    if arr[mid]==x:
        return mid
    elif arr[mid]<x:
        return search(arr,x,mid+1,h)
    elif arr[mid]>x:
        return search(arr,x,l,mid-1)
    
    return -1


arr = [5,10,15,20,25,30,35,40,45,50,55,60]

index = search(arr,15,0,len(arr)-1)

if(index==-1):
    print('Not found')
else:
    print(f'Number present at index {index}')

# Time Complexity: 
# -> Best Case: O(1)
# -> Average Case: O(log N)
# -> Worst Case: O(log N)
# Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(log N).