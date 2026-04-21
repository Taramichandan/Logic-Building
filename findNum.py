def findNum(arr) :

    n = arr[0]

    largest = 0
    smallest = 0

    for num in arr :

        if num > n :
            largest = num

        elif num < n :
            smallest = num

    return largest  , smallest      


print(findNum([8,4,5,9,10,24]))