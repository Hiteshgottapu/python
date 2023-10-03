def bu(arr):
    n =len(arr)
    for i in range (n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
    return arr
arr=[78 , 23 , 12 , 90 ]
print("Before sorting : ",arr)
print ('Array after sorting :',bu(arr ))
