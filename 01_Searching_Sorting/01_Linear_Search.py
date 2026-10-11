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