def rotArr (arr) :
    
    first = arr[0]

    for num in range(len(arr) - 1):

        arr[num] = arr[num + 1]

    arr[-1] = first    

    return arr
        

print(rotArr([1,2,3,4,5]))