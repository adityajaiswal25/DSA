def array(arr,left,right):
    if left>= right :
        return arr
    arr[left],arr[right] = arr[right],arr[left]
    return array(arr,left+1,right-1)
print(array([1,2,3,4,5],1,3))