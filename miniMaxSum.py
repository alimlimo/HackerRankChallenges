def miniMaxSum(arr):
    arr4=arr[0]+arr[1]+arr[2]+arr[3]
    arr0=arr[4]+arr[1]+arr[2]+arr[3]
    arr1=arr[0]+arr[4]+arr[2]+arr[3]
    arr2=arr[0]+arr[4]+arr[1]+arr[3]
    arr3=arr[0]+arr[4]+arr[2]+arr[1]
    a=[arr0,arr1,arr2,arr3,arr4]
    max_arr=arr0
    min_arr=arr0
    for i in range(0,5):
        if max_arr < a[i]:
            max_arr = a[i]
        elif min_arr > a[i]:
            min_arr = a[i]
    print(min_arr, max_arr)